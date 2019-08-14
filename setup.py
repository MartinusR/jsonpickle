#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Modified by Martin Ruffel.
# Copyright (C) 2008 John Paulett (john -at- paulett.org)
# Copyright (C) 2009-2017 David Aguilar (davvid -at- gmail.com)
# All rights reserved.
#
# This software is licensed as described in the file COPYING, which
# you should have received as part of this distribution.

import os
try:
    import setuptools as setup_mod
except ImportError:
    import distutils.core as setup_mod

here = os.path.dirname(__file__)
version = os.path.join(here, 'jsonpickle', 'version.py')
scope = {}
exec(open(version).read(), scope)

SETUP_ARGS = dict(
    name='jsonpickle',
    version=scope['__version__'],
    description=(
        'Python library for serializing any arbitrary object graph into JSON'),
    long_description=(
        'jsonpickle converts complex Python objects to and from JSON.'),
    author='Martin Ruffel',
    author_email='martin.ruffel@ens.fr',
    url='https://github.com/MartinusR/jsonpickle/',
    license='BSD',
    platforms=['POSIX', 'Windows'],
    keywords=['json pickle', 'json', 'pickle', 'marshal',
              'serialization', 'JavaScript Object Notation'],
    classifiers=[
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Programming Language :: Python',
    ],
    options={'clean': {'all': 1}},
    packages=['jsonpickle', 'jsonpickle.ext'],
)


if __name__ == '__main__':
    setup_mod.setup(**SETUP_ARGS)
