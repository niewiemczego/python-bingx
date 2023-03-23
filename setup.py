import os

from setuptools import setup

about = {}
here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, "bingx", "__version__.py"), "r") as f:
    exec(f.read(), about)

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name=about["__title__"],
    version=about["__version__"],
    author=about["__author__"],
    description=about["__description__"],
    license=about["__license__"],
    packages=['bingx'],
    description='BingX REST API python implementation',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/niewiemczego/python-bingx',
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