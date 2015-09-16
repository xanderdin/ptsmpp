#!/usr/bin/env python

import os
from setuptools import setup, find_packages


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name = "ptsmpp",
    version = "0.1.0",
    author = "Alexander Pravdin",
    author_email = "aledin@mail.ru",
    description = "PTSMPP - Python Twisted SMPP 3.4 client library",
    license = 'Apache License 2.0',
    packages = find_packages(),
    long_description=read('README.md'),
    keywords = "ptsmpp smpp twisted",
    url = "https://github.com/xanderdin/ptsmpp",
    include_package_data = True,
    package_data={
        'ptsmpp': ['README.md'],
        'ptsmpp': ['LICENCE'],
        'ptsmpp': ['requirements.txt'],
    },
    zip_safe = False,   
    install_requires = [
        'twisted',
        'pyOpenSSL',
    ],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Framework :: Twisted",
        "Topic :: System :: Networking",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: Apache Software License",
        "Intended Audience :: Developers",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)

