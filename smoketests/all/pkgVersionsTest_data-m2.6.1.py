#!/usr/bin/env python

monoVersion = "2.6.1.0"
monoShortVersion = "2.6.1"

# These packages are common across all platforms
pkgs = {
    #'pkg-config --modversion atk':  '1.24.0',
    'pkg-config --modversion mono-cairo':       monoShortVersion,
    'pkg-config --modversion mono-lineeditor':  '0.2.1',
    'pkg-config --modversion mono-nunit':       monoShortVersion,
    'pkg-config --modversion mono-options':     '0.2.1',
    'pkg-config --modversion mono.web':         '2.0.0.0',
    'pkg-config --modversion monodoc':          monoShortVersion,
    'pkg-config --modversion xsp':              '2.6',
    'pkg-config --modversion mono':             monoShortVersion,
}

# These packages are unique to linux
linux_pkgs = {
    'pkg-config --modversion gtk-sharp-2.0':    '2.12.9',
    'pkg-config --modversion gnome-sharp-2.0':  '2.24.1',
    'pkg-config --modversion mono-addins':      '0.4',
    'pkg-config --modversion mono-addins-gui' : '0.4',
    'pkg-config --modversion mono-addins-setup':'0.4',
    'pkg-config --modversion mono-zeroconf':    '0.9.0',
    'pkg-config --modversion monodevelop':      '2.2',
    'pkg-config --modversion monodevelop-core-addins':'2.2',
}

# These packages are unique to linux
monovs_linux_pkgs = {
    'pkg-config --modversion gtk-sharp-2.0':    '2.12.6',
    'pkg-config --modversion gnome-sharp-2.0':  '2.24.0',
}


# These packages are unique to OSX
macos_pkgs = { 
    'pkg-config --modversion gtk-sharp-2.0':    '2.12.9',
    'pkg-config --modversion cocoa-sharp':      '0.9.5',
    'pkg-config --modversion mono-addins':      '0.4',
    'pkg-config --modversion mono-addins-gui' : '0.4',
    'pkg-config --modversion mono-addins-setup':'0.4',

}

# These packages are unique to win32
win32_pkgs = {
    'pkg-config --modversion gtk-sharp-2.0':    '2.12.9',
}


# These executables are common across all platforms
exes = {
    'mono --version':               monoShortVersion,
    'mcs --version':                monoVersion,
    'gmcs --version':               monoVersion,
    'xsp --version':                '2.6.0.0',
    'xsp1 --version':               '2.6.0.0',
    'xsp2 --version':               '2.6.0.0',
    'monolinker --version':         '0.2.0.0',
    'resgen --version':             monoVersion,
    'resgen1 --version':            monoVersion,
    'resgen2 --version':            monoVersion,
    'mod-mono-server --version':    '2.6.0.0',
    'mod-mono-server1 --version':   '2.6.0.0',
    'mod-mono-server2 --version':   '2.6.0.0',
    'signcode --version':           monoVersion,
    'csharp --version':             '2.1.0.0',
    'al --version':                 monoVersion,
    'al1 --version':                monoVersion,
    'al2 --version':                monoVersion,
    'ilasm --version':              monoVersion,
    'ilasm1 --version':             monoVersion,
    'ilasm2 --version':             monoVersion,
}

# These executables are unique to linux
linux_exes = {
}

# These executables are unique to OSX
macos_exes = {
    'monodocer --version':          '0.1.0',
    'mconfig --version':            '0.1.0.0',
    'monodis':                                       'Disassembler',
    'monograph --version':                           '0.2',
    'pango-querymodules --version':                  '1.22.4',
    'pkg-config --version':                          '0.23',
    'booc --version':                                '0.9.1.3287',
    'caspol':                                        monoVersion,
    'certmgr':                                       monoVersion,
    'chktrust':                                      monoVersion,
    'disco':                                         monoVersion,
    'fastcgi-mono-server --version':                 '2.6.0.0',
    'fastcgi-mono-server1 --version':                '2.6.0.0',
    'fastcgi-mono-server2 --version':                '2.6.0.0',
    'ipy -V':                                        '1.1',
    'ipy2 -V':                                       '2.0A5',
    'makecert':                                      monoVersion,
    'mdoc --version':                                '0.1.0',
}

# These executables are unique to win32
win32_exes = {
    'envsubst --version':                            '0.17',
    'gdk-pixbuf-csource --version':                  '2.18.3',
    'glib-genmarshal --version':                     '2.22.2',
    'monodis':                                       'Disassembler',
    'monograph --version':                           '0.2',
    'msgfmt --version':                              '0.17',
    'pango-querymodules --version':                  '1.26.0',
    'pkg-config --version':                          '0.23',
    'recode-sr-latin.exe --version':                 '0.17',
    'booc --version':                                '0.9.2.3383',
    'caspol':                                        monoVersion,
    'certmgr':                                       monoVersion,
    'chktrust':                                      monoVersion,
    'disco':                                         monoVersion,
    'fastcgi-mono-server --version':                 '2.6.0.0',
    'fastcgi-mono-server1 --version':                '2.6.0.0',
    'fastcgi-mono-server2 --version':                '2.6.0.0',
    'gendarme --version':                            monoVersion,
    'ikvm -version':                                 '0.40.0.1',
    'ipy -V':                                        '1.1',
    'ipy2 -V':                                       '2.0A5',
    'makecert':                                      monoVersion,
    'mdoc --version':                                monoVersion,
    'mjs --version':                                 '0.0.0.0',
    'monolinker --version':                          '0.2.0.0',
    'monop --runtime-version':                       '2.0.50727.1433',
    'monop1 --runtime-version':                      '1.1.4322.2032',
    'monop2 --runtime-version':                      '2.0.50727.1433',
    'nant':                                          '0.86',
    'nunit-console':                                 '2.4.8',
    'nunit-console2':                                '2.4.8',
    'permview':                                      monoVersion,
    'prj2make --version':                            monoVersion,
    'secutil':                                       monoVersion,
    'setreg':                                        monoVersion,
    'sgen':                                          '2.0.50727.1433',
    'signcode':                                      monoVersion,
    'sn':                                            monoVersion,
    'vbnc':                                          '0.0.0.5917',
    'xbuild --version':                              monoVersion,
}

# vim:ts=4:expandtab:
