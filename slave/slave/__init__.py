#!/usr/bin/env python

from fabric.api import run, env

def funtimes():
    global env
    print 'env.hosts =', env.hosts
    run('echo Hello funtimes')
