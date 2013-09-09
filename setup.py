#!/usr/bin/env python

from distutils.core import setup, find_packages

version = '0.1'

setup(
    name='python-national-identification-number',
    version=version,
    description='This Python library aims to provide simple authentication of various national identification numbers.',
    author='Henrik Ossipoff Hansen',
    author_email='henrik.ossipoff@gmail.com',
    url='https://github.com/HenrikOssipoff/python-national-identification-number',
    packages=find_packages(),
    install_requires=['distribute']
)