#!/usr/bin/env python

import sys
import os
import subprocess
import pdb

myTestopia = None

def checkOption(option,name):
    '''This function checks that an option has been set
       in the config file or on the command line.'''
    if option == None:
        msg = '''Config option '%s' is not set.
Add '%s = <somevalue>' to defaults.conf 
 or set it on the command line. See --help''' %(name,name)
        printColor(msg,'red')

        raise Exception("Config option '%s' is not set" % name)

def printColor(msg, color):
    printColorOnOS(msg, color)

def executeCmd(command, stderr=open(os.devnull)):
    ret = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=stderr)
    output = ret.communicate()[0]
    lines = output.split('\n')
    return lines

def whichOS():
    if sys.platform == 'win32':
        return 'win32'
    elif sys.platform == 'linux2':
        if os.path.isfile("/studio/profile"):
            # this will determine if it's running on vpc
            moboMaker = executeCmd("hal-device computer | grep system.board.vendor")[0].strip()

            # this tells us what type if image kiwi created (VM or LiveCD)
            for curLine in open("/studio/profile").readlines():
                if "kiwi_type=" in curLine:
                    kiwiType = curLine.split("=")[1].strip().strip("\"")

            if moboMaker == "system.board.vendor = 'Microsoft Corporation'  (string)" and kiwiType == "vmx":
                return 'vpc'
            elif kiwiType == "iso":
                return 'livecd'
            elif kiwiType == "vmx":
                return 'vmware'
            else:
                raise Exception("Couldn't determine the type of kiwi created image I'm running on.")
        else:
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
