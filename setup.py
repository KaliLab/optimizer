# -*- coding: utf-8 -*-
import sys
import getopt
import shutil
from distutils.core import setup
import os

setup(
#    data_files=[('optimizer/)],
    name = "optimizer",
    version = '0.0.1alpha',
    packages = ['optimizer'],
    package_data = {'optimizer': ['*.png']},
    author = "Optimizer authors and contributors",
    author_email = "vellamike@gmail.com",
    description = "A Python library for optimization of neuronal models",
#    long_description = long_description,
    license = "BSD",
    url="http://optimizer.readthedocs.org/en/latest/",
    classifiers = [
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Topic :: Scientific/Engineering']
)

if os.name == 'posix':
    script_dir = '/usr/bin'
