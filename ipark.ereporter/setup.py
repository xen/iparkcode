from setuptools import setup

setup(
    name = "ipark.ereporter",
    version = "0.2",
    description = 'Send exceptions via mail',
    author = 'Ilya Petrov',
    author_email = 'petrov@iparkcorp.com',
    url = 'http://code.google.com/p/iparkcode/',
    packages = ['ipark', 'ipark.ereporter', ],
    license = "BSD",
    scripts=[],
    install_requires = [
        'tipfy==0.6', 
    ],
)
