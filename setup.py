# coding: utf-8

"""
    Bricklink REST API client
"""


from setuptools import setup, find_packages  # noqa: H301

NAME = "py-bricklink"
VERSION = "0.1.0"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = ["rauth"]

setup(
    name=NAME,
    version=VERSION,
    description="Bricklink REST API client",
    author_email="",
    url="",
    keywords=["Bricklink"],
    install_requires=REQUIRES,
    packages=find_packages(),
    include_package_data=True,
    long_description="""\
    Bricklink REST API Client # noqa: E501
    """
)
