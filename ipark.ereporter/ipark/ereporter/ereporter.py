import os
from google.appengine.api.labs.taskqueue import Task
import logging
from tipfy import RequestHandler, Response, get_config, Tipfy
from google.appengine.api import mail
from google.appengine.ext.ereporter import ExceptionRecordingHandler
from pprint import pformat

def report(exc_info):
    signature = ExceptionRecordingHandler._ExceptionRecordingHandler__GetSignature(exc_info)
    trace = logging._defaultFormatter.formatException(exc_info)

    e, _u, t = exc_info

    code = t.tb_frame.f_code

    _report = str(trace) + \
        "\n\nVars:\n" + pformat(t.tb_frame.f_locals)

    return (_report, signature)

class Handler(logging.Handler):
  def emit(self, record):
    if not record.exc_info:
      return
    request = getattr(Tipfy, 'request', None) if Tipfy is not None else None
    if request and request.headers.get('X-AppEngine-QueueName') \
      == 'error-report':
        return

    try:
      trace, subject = report(record.exc_info)

      t = Task(
          url = "/internal/ereporter",
          params = dict(trace = trace, subject = subject),
      )
      t.add("error-report")
    except:
      pass


def register_logger(logger = None):
  if not logger:
    logger = logging.getLogger()
  handler = Handler()
  logger.addHandler(handler)
  return handler


class SendReport(RequestHandler):
  def post(self):
    trace = self.request.form.get("trace")
    subject = self.request.form.get("subject")

    mail.send_mail(
        sender = get_config(__name__, "email"),
        to = get_config(__name__, "email"),
        subject = "[trace] %s" % subject,
        body = trace,
    )

    return Response("nyyaaa")
