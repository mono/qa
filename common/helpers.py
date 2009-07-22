#!/usr/bin/env python

import sys
import subprocess


def printColor(msg, color):
    printColorOnOS(msg, color)

def executeCmd(command):
    ret = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
    output = ret.communicate()[0]
    lines = output.split('\n')
    return lines

def whichOS():
    if sys.platform == 'win32':
        return 'win32'
    elif sys.platform == 'linux2':
        return 'linux'
    elif sys.platform == 'darwin':
        return 'macos'

def getPrefix():
    myos = whichOS()
    if myos == 'win32':
        return ''
    elif myos == 'linux':
        return ''
    elif myos == 'macos':
        return '/Library/Frameworks/Mono.framework/Versions/Current/bin/'


if whichOS() == 'win32':
    from winColors import printColor as printColorOnOS
else:
    from uxColors import printColor as printColorOnOS

# vim:ts=4:expandtab:
