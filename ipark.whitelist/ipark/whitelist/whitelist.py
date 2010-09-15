from tipfy import Response, Tipfy, get_config
""" White list access

Add to your config.py section with list of ip that you allow to access.


config['ipark.whitelist'] = {
  'allow_ips' : [ '192.168.1.%', # local users
      '127.0.0.1', 
      '1.2.3.100', # My home IP
  ]
}
"""

allow_ips = get_config('ipark.whitelist', 'allow_ips')

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

class WhiteList(object):
  def pre_dispatch(self, handler):
        # gather some info
        ip = getIP(Tipfy.request)

        for allowed in allow_ips:
          if cmpIP(allowed, ip):
            return

        return forbidden_page

