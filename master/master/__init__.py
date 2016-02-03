#!/usr/bin/env python

__author__ = 'Alec Taylor'
__version__ = '0.0.1'

from os import environ

from fabric.api import execute, env

from slave import funtimes

env.key_filename = environ['PRIVATE_QUAY_PATH']
env.hosts = ['ec2-omitted.compute.amazonaws.com']
env.user = 'ubuntu'

def inn():
    def innnn():
        execute(funtimes)
    return innnn

if __name__ == '__main__':
    inn()()
