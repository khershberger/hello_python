try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(name = 'hello',
    description = 'Hello World test package',
    authon = 'Me',
    version = '0.1',
    packages = ['hello'],
    install_requires = [ ]
    )
