'''
Created on 2017年8月20日

@author: sunshyran
'''

import sys

from setuptools import setup, find_packages

VERSION="1.0.a"

setup(name         = 'PythonRpcFramework',
      version      = VERSION,
      description  = 'A easy rpc framework with protocol json-rpc-2.0',
      long_description = "",
      author       = 'sunshyran',
      author_email = 'sunshyran@gmail.com',
      url          = 'https://github.com/sunshyran/PythonRpcFramework',
      license      = 'Apache License 2.0',
      keywords     = 'rpcframework python json',
      platforms    = 'any',
      classifiers  = [
                        "License :: OSI Approved :: Apache Software License",
                        "Operating System :: OS Independent",
                        "Programming Language :: Python",
                     ],
      install_requires = [
                         ],
      packages     = find_packages(),
      include_package_data = True,
      )
if __name__ == '__main__':
    pass