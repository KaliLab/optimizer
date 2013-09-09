# -*- coding: utf-8 -*-

from distutils.core import setup

with open('requirements.txt') as f:
    required = f.read().splitlines()

long_description = open("README.md").read()

setup(
    data_files=[()],
    install_requires=required,
    name = "optimizer",
    version = '0.0.1alpha',
    packages = ['optimizer'],
#    package_data = {'neuroml.test': ['*.nml']},
    author = "libNeuroML authors and contributors",
    author_email = "vellamike@gmail.com",
    description = "A Python library for optimization of neuronal models",
    long_description = long_description,
    license = "BSD",
    url="http://libneuroml.readthedocs.org/en/latest/",
    classifiers = [
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Topic :: Scientific/Engineering']
)
