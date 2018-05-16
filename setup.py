#-*- encoding: UTF-8 -*-
from setuptools import setup, find_packages
import sys, json
"""
打包的用的setup必须引入，
"""
VERSION = '0.0.3'
setup(name='youdao.cli',
      version=VERSION,
      description="A youdao simple douban cli based on Python",
      long_description='just enjoy',
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='python youdao youdao.cli terminal',
      author='xiaozhizi1',
      author_email='349940031@qq.com',
      url='',
      license='MIT',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=True,
      install_requires=[
        'clint',
        'requests',
      ],
      entry_points={
        'console_scripts':[
            'youdai = youdao.cli:main'
        ]
      },
)