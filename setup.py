import os
import subprocess
from setuptools import setup, find_packages

setup(
    name='lipids',
    version='0.0.0',
    author='Timothy C. Moore',
    author_email='tcmoore3@gmail.com',
    packages=find_packages(),
    url='http://github.com/tcmoore3/lipids',
    description='My lipid molecules for building lipid systems.',
    long_description=open('README.md').read(),
    install_requires=[
    "mbuild",
    ],
)
