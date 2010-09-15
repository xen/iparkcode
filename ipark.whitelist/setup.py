"""
ipark.whitelist
===============

tipfy middleware that restrict access to site from any IP unless it from white list.

Setup
-----

To use this extension in your application follow few simple steps:

* To buildout.cfg add `ipark.whitelist` egg import
* Modify config.py and add folowing lines::

  #
  config['ipark.whitelist'] = {
    # use %  as mask
    'allow_ips' : [ '192.168.1.%', 
        '195.138.76.153', 
        '127.0.0.1', 
  }
"""


from distutils.core import setup

setup(
    name = "ipark.whitelist",
    version = "0.2.5",
    description = 'Tipfy middleware extension to whitelist access by IP',
    long_description = __doc__,
    zip_safe = False,
    author = 'Ilya Petrov, Mikhail Kashkin',
    author_email = 'mk@iparkcorp.com',
    url = 'http://code.google.com/p/iparkcode/',
    packages = ['ipark', 'ipark.whitelist', ],
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
