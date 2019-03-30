# -*- coding: utf-8 -*-
# Zilliqa Python API
# Copyright (C) 2019  Gully Chen
# MIT License
"""
setup file
"""

from pyzil import version
from setuptools import setup, find_packages

packages = find_packages()
package_data = {"pyzil": ["tests/*", "tests/crypto/*"]}

tests_require = ["pytest"]
install_requires = [
    "requests", "jsonrpcclient", "jsonrpcclient[requests]",
    "protobuf", "fastecdsa", "pyethash",
    "pycryptodome", "eth-hash[pycryptodome]",
]

setup(
    name="pyzil",
    version=version,
    description="Zilliqa Python API",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Programming Language :: Python"
    ],
    keywords="zilliqa api",
    author="Gully Chen",
    author_email="deepgully@gmail.com",
    url="",
    license="MIT License",
    packages=packages,
    include_package_data=True,
    package_data=package_data,
    install_requires=install_requires,
    tests_require=tests_require,
)
