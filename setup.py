#!/usr/bin/env python

from setuptools import setup
from perceptron import __author__, __version__

import os
import sys

setup(
    name = 'perceptron',
    version = __version__,
    author = 'Roger Fernandez Guri',
    author_email = 'rfguri@gmail.com',
    license = open('LICENSE').read(),
    url = 'https://github.com/rfguri/perceptron/',
    keywords = 'ml machine learning neuralnetworks mlp python nn',
    description = 'Multilayer perceptron network implementation in Python',
    long_description = open('README.rst').read(),
    include_package_data = True,
    packages = (
        'perceptron',
    ),
    classifiers = (
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
    )
)

