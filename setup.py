import codecs
import os
import re

from setuptools import setup

with codecs.open(
        os.path.join(
            os.path.abspath(os.path.dirname(__file__)),
            'bingx',
            '__init__.py'
        ), 'r', 'latin1') as fp:
    try:
        version = re.findall(r'^__version__ = "([^"]+)"\r?$', fp.read(), re.M)[0]
    except IndexError:
        raise RuntimeError('Unable to determine version...')

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='python-bingx',
    version=version,
    packages=['bingx'],
    description='BingX REST API python implementation',
    long_description=long_description,
    long_description_content_type="text/x-rst",
    url='https://github.com/niewiemczego/python-bingx',
    author='niewiemczego',
    license='MIT',
    author_email='',
    install_requires=[
        'requests', 'websockets'
    ],
    keywords='bingx exchange rest api bitcoin ethereum btc eth',
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)