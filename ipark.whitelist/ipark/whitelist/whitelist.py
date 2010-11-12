from tipfy import Response, get_config
""" White list access

Add to your config.py section with list of ip that you allow to access.


config['ipark.whitelist'] = {
  'allow_ips' : [ '192.168.1.%', # local users
      '127.0.0.1',
      '1.2.3.100', # My home IP
  ],
  'allow_paths' : ['/path1', '/path2','/%/path3'],
}
"""

allow_ips = get_config('ipark.whitelist', 'allow_ips')
allow_paths = get_config('ipark.whitelist', 'allow_paths', [])

forbidden_page = Response("""
    <html>
    <head>
        <title>403 Forbidden</title>
    </head>
    <body>
        <h1>403 Forbidden</h1>
        <p>This resource is unavailable at this time from this computer.</p>
    </body>
    </html>""",
    status = 403,
    content_type = "text/html",
)

vsplits = lambda x: x.replace('%', '').split('.')
zsplits = lambda x: x.replace('%', '').split('/')

def getIP(req):
  ip = req.remote_addr
  # forwarded proxy fix for webfaction
  xff = req.headers.get("X-Forwarded-For")
  if (not ip or ip == '127.0.0.1') and xff:
    ip = xff
  return ip

def cmpIP(x, y):
  # Returns boolean whether or not the ip matterns match, % is a wildcard
  x = vsplits(x); y = vsplits(y)
  for i in range(4):
    if x[i] and y[i] and x[i] != y[i]:
      return False
  return True

def cmpPath(x, y):
  x = zsplits(str(x)); y = zsplits(str(y))
  if len(x) == len(y):
    for i in range(len(x)):
      if x[i] and y[i] and x[i] != y[i]:
        return False
    return True
  return False

class WhiteList(object):

  def pre_dispatch(self, handler):
    for allowed in allow_paths:
      if cmpPath(allowed, handler.request.path):
        return
    ip = getIP(handler.request)
    for allowed in allow_ips:
      if cmpIP(allowed, ip):
        return
    return forbidden_page

