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



# vim:ts=4:expandtab:
