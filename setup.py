import ez_setup
ez_setup.use_setuptools()

from setuptools import setup, find_packages

setup(name='MyPackage',
      version='0.1.0',
      author='Zulko',
    description='',
    long_description=open('README.rst').read(),
    license='see LICENSE.txt',
    keywords="",
    packages= find_packages(exclude='docs'))
