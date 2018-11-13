# -*- coding: utf-8 -*-

# Learn more: https://github.com/kennethreitz/setup.py

from setuptools import setup, find_packages

with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='small-world',
    version='0.0.1',
    description='Experimenting AI',
    long_description=readme,
    author='Kineolyan',
    author_email='kineolyan@gmail.com',
    url='https://github.com/Kineolyan/small-world',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)