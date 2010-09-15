"""ipark.ereporter
================

Usefull tipfy extension that send developer every exeption traceback report by email. 
Its very handy when you beta test your projects and dont sure if something is going wrong.

Setup
------

To use this extension in your application follow few simple steps:

* Add to buildout.cfg egg import
* Modify config.py and add folowing lines::

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


"""
from setuptools import setup

setup(
    name = "ipark.ereporter",
    version = "0.2.3",
    description = 'Tipfy extension to simplify projects beta test, it simply send all exceptions traceback via'+\
      ' email to application administrators',
    long_description = __doc__,
    zip_safe = False,
    author = 'Ilya Petrov, Mikhail Kashkin',
    author_email = 'mk@iparkcorp.com',
    url = 'http://code.google.com/p/iparkcode/',
    packages = ['ipark', 'ipark.ereporter', ],
    license = "BSD",
    scripts=[],
    install_requires = [
        'tipfy>=0.6, <0.7', 
    ],
    classifiers = [
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)
