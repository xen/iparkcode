# ipark.ereporter #

Usefull tipfy extension that send developer every exeption traceback report by email. 
Its very handy when you beta test your projects and dont sure if something is going wrong.

## Setup ##

To use this extension in your application follow few simple steps:

- Add to buildout.cfg egg import
- Modify config.py and add folowing lines:

# List of installed apps
config['tipfy'] = {
    'apps_installed': [
      ...
      'ipark.ereporter',
      ...
     ]
 }

#
config['ipark.ereporter.ereporter'] = {
     'email' : 'XXX@domain.com', # Use developer's email as it is free to send 
}

# 