#!/usr/bin/python

# These packages are common across all platforms
pkgs = {
    #'pkg-config --modversion atk':  '1.24.0',
    'pkg-config --modversion gtk-sharp-2.0':    '2.12.9',
    'pkg-config --modversion mono':             '2.4.2.3',
    'pkg-config --modversion mono-cairo':       '2.4.2.3',
    'pkg-config --modversion mono-lineeditor':  '0.2.1',
    'pkg-config --modversion mono-nunit':       '2.4.2.3',
    'pkg-config --modversion mono-options':     '0.2.1',
    'pkg-config --modversion mono.web':         '2.0.0.0',
    'pkg-config --modversion monodoc':          '2.4.2.3',
    'pkg-config --modversion smcs':             '2.4.2.3',
    'pkg-config --modversion xsp':              '2.4.2',
}

# These packages are unique to linux
linux_pkgs = {
    'pkg-config --modversion gnome-sharp-2.0':  '2.24.0',
    'pkg-config --modversion mono-addins':      '0.4',
    'pkg-config --modversion mono-addins-gui' : '0.4',
    'pkg-config --modversion mono-addins-setup':'0.4',
    'pkg-config --modversion mono-zeroconf':    '0.8.0',
    'pkg-config --modversion monodevelop':      '2.0',
    'pkg-config --modversion monodevelop-core-addins':'2.0',
}


# These packages are unique to OSX
macos_pkgs = { 
    'pkg-config --modversion cocoa-sharp':      '0.9.5',
    'pkg-config --modversion mono-addins':      '0.4',
    'pkg-config --modversion mono-addins-gui' : '0.4',
    'pkg-config --modversion mono-addins-setup':'0.4',

}

# These packages are unique to win32
win32_pkgs = {
}


# These executables are common across all platforms
exes = {
    'mono --version':               '2.4.2.3',
    'mcs --version':                '2.4.2.3',
    'gmcs --version':               '2.4.2.3',
    'smcs --version':               '2.4.2.3',
    'xsp --version':                '2.4.2.0',
    'xsp1 --version':               '2.4.2.0',
    'xsp2 --version':               '2.4.2.0',
    'monolinker --version':         '0.2.0.0',
    'resgen --version':             '2.4.2.3',
    'resgen1 --version':            '2.4.2.3',
    'mod-mono-server --version':    '2.4.2.0',
    'signcode --version':           '2.4.2.3',
    'csharp --version':             '2.4.2.3',
    'al --version':                 '2.4.2.3',
    'al1 --version':                '2.4.2.3',
    'al2 --version':                '2.4.2.3',
    'ilasm --version':              '2.4.2.3',
    'ilasm1 --version':             '2.4.2.3',
    'ilasm2 --version':             '2.4.2.3',
}

# These executables are unique to linux
linux_exes = {
}

# These executables are unique to OSX
macos_exes = {
    'monodocer --version':          '0.1.0',
    'mconfig --version':            '0.1.0.0',
}

# These executables are unique to win32
win32_exes = {
    'envsubst --version':              '0.17',
}

# vim:ts=4:expandtab:
