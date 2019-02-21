# -*- coding: UTF-8 -*-
import os

from setuptools import setup
from setuptools.command.test import test
from codecs import open

setup_dir = os.path.abspath(os.path.dirname(__file__))


def read(file_name):
    return open(os.path.join(setup_dir, file_name), 'r', encoding='utf-8').read()


class Test(test):

    def run_tests(self):
        import unittest

        test_loader = unittest.defaultTestLoader
        test_runner = unittest.TextTestRunner()
        test_suite = test_loader.discover(setup_dir)
        test_runner.run(test_suite)


setup(
    name='mybatis-mapper2sql',
    version='0.1.4',
    author='hhyo',
    author_email='rtttte@qq.com',
    url='http://github.com/hhyo/mybatis-mapper2sql',
    description='Generate SQL Statements from the MyBatis3 Mapper XML file',
    long_description=read('README.md'),
    long_description_content_type='text/markdown',
    keywords='mybatis mapper2sql mybatis-mapper2sql',
    packages=['mybatis_mapper2sql'],
    include_package_data=True,
    install_requires=[
        'sqlparse==0.2.4'
    ],
    license='Apache 2.0',
    zip_safe=False,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    cmdclass={'test': Test}
)
