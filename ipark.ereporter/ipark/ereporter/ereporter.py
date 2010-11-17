import os
import logging
from tipfy import RequestHandler, Response, get_config, Tipfy
from google.appengine.api import mail
from google.appengine.ext.ereporter import ExceptionRecordingHandler
from google.appengine.ext.deferred import defer
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

      defer(send_report, trace, subject)
    except:
      pass


def register_logger(logger = None):
  if not logger:
    logger = logging.getLogger()
  handler = Handler()
  logger.addHandler(handler)
  return handler

try:
  get_config(__name__, "email")
  print "XXX: Config variables path was changed opdate your config.py and change to ipark.ereporter"
except:
  pass

def send_report(trace, subject):
  mail.send_mail(
      sender = get_config('ipark.ereporter', "email"),
      to = get_config('ipark.ereporter', "email"),
      subject = "[trace] %s" % subject,
      body = trace,
  )
