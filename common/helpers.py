#!/usr/bin/env python

import subprocess

def executeCmd(command):
    ret = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
    output = ret.communicate()[0]
    lines = output.split('\n')
    return lines

# vim:ts=4:expandtab:
