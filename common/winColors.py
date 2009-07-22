#!/usr/bin/python

import ctypes

colors = {
        'red':0x0004,
        'green':0x0002,
        'orange':0x0006,
        'blue':0x0001,
        'purple':0x0005,
}


## Constants from the Windows API
STD_OUTPUT_HANDLE = -11
#FOREGROUND_BLACK     = 0x0000
#FOREGROUND_BLUE      = 0x0001
#FOREGROUND_GREEN     = 0x0002
#FOREGROUND_CYAN      = 0x0003
#FOREGROUND_RED       = 0x0004
#FOREGROUND_MAGENTA   = 0x0005
#FOREGROUND_YELLOW    = 0x0006
#FOREGROUND_GREY      = 0x0007
FOREGROUND_INTENSITY = 0x0008 # foreground color is intensified.
#
#BACKGROUND_BLACK     = 0x0000
#BACKGROUND_BLUE      = 0x0010
#BACKGROUND_GREEN     = 0x0020
#BACKGROUND_CYAN      = 0x0030
#BACKGROUND_RED       = 0x0040
#BACKGROUND_MAGENTA   = 0x0050
#BACKGROUND_YELLOW    = 0x0060
#BACKGROUND_GREY      = 0x0070
#BACKGROUND_INTENSITY = 0x0080 # background color is intensified.

def get_csbi_attributes(handle):
    # Based on IPython's winconsole.py, written by Alexander Belchenko
    import struct
    csbi = ctypes.create_string_buffer(22)
    res = ctypes.windll.kernel32.GetConsoleScreenBufferInfo(handle, csbi)
    assert res

    (bufx, bufy, curx, cury, wattr,
    left, top, right, bottom, maxx, maxy) = struct.unpack("hhhhHhhhhhh", csbi.raw)
    return wattr

def printColor(msg, color):
    handle = ctypes.windll.kernel32.GetStdHandle(STD_OUTPUT_HANDLE)
    reset = get_csbi_attributes(handle)
    ctypes.windll.kernel32.SetConsoleTextAttribute(handle, colors[color] | FOREGROUND_INTENSITY)
    print msg
    ctypes.windll.kernel32.SetConsoleTextAttribute(handle, reset)
