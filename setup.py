"""Setup.py"""
from setuptools import setup, find_packages


setup(
    name='logger',
    version=1.0,
    packages=find_packages(),
    include_package_data=True,
    install_requires=['colorlog'],
    author='jneo8',
    author_email='james0910238727@gmail.com',
    description='Just a logger',
    url='https://github.com/jneo8/base_conf',
)
