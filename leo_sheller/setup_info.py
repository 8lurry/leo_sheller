# -*- coding: UTF-8 -*-
# Copyright 2022 8lurry <sharifmehedi24@outlook.com>
# License: GNU Affero General Public License v3 (see file COPYING for details)

SETUP_INFO = dict(
    name='leo-sheller',
    version='0.1.0-alpha',
    # install_requires=['lino-xl'],
    description=("Simple sheller."),
    author='8lurry',
    author_email='sharifmehedi24@outlook.com',
    # url="https://gitlab.com/lino-framework/medico",
    license_files=['COPYING'],
    # test_suite='tests'
)

SETUP_INFO.update(classifiers="""
Programming Language :: Python
Programming Language :: Python :: 3
Development Status :: 1 - Alpha
Environment :: Shell Environment
Framework :: leo
Intended Audience :: AI community
Intended Audience :: Physics community
Intended Audience :: Hacker community
License :: OSI Approved :: GNU Affero General Public License v3
Operating System :: OS Independent
Topic :: Shelling
""".format(**SETUP_INFO).strip().splitlines())
SETUP_INFO.update(packages=[
])
