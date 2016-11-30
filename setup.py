#!/usr/bin/env python
# -*- coding: utf-8 -*-

# {# pkglts, pysetup.kwds
# format setup arguments

from setuptools import setup, find_packages


short_descr = "belle petite description"
readme = open('README.rst').read()
history = open('HISTORY.rst').read().replace('.. :changelog:', '')


# find version number in src/py3djsx/version.py
version = {}
with open("src/py3djsx/version.py") as fp:
    exec(fp.read(), version)


setup_kwds = dict(
    name='py3djsx',
    version=version["__version__"],
    description=short_descr,
    long_description=readme + '\n\n' + history,
    author="Christophe Pradal, Simon Artzet, ",
    author_email="@pradal, @artzet-s, ",
    url='https://github.com/Christophe Pradal/py3djsx',
    license='cecill-c',
    zip_safe=False,

    packages=find_packages('src'),
    package_dir={'': 'src'},
    install_requires=[
        ],
    tests_require=[
        "mock",
        "nose",
        ],
    entry_points={},
    keywords='',
    test_suite='nose.collector',
)
# #}
# change setup_kwds below before the next pkglts tag

# do not change things below
# {# pkglts, pysetup.call
setup(**setup_kwds)
# #}
