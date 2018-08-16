import os
import subprocess
from setuptools import setup, find_packages

setup(
    name='lipids',
    version='0.0.0',
    author='Timothy C. Moore and Parashara Shamaprasad',
    author_email='p.shama@vanderbilt.edu',
    packages=find_packages(),
    url='http://github.com/uppittu11/lipids',
    description='My lipid molecules for building lipid systems.',
    long_description=open('README.md').read(),
    install_requires=[
    "mbuild",
    ],
)
