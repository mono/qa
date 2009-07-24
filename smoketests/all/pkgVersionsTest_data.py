#!/usr/bin/python

monoVersion = "2.4.2.3"

# These packages are common across all platforms
pkgs = {
    #'pkg-config --modversion atk':  '1.24.0',
    'pkg-config --modversion gtk-sharp-2.0':    '2.12.9',
    'pkg-config --modversion mono-cairo':       monoVersion,
    'pkg-config --modversion mono-lineeditor':  '0.2.1',
    'pkg-config --modversion mono-nunit':       monoVersion,
    'pkg-config --modversion mono-options':     '0.2.1',
    'pkg-config --modversion mono.web':         '2.0.0.0',
    'pkg-config --modversion monodoc':          monoVersion,
    'pkg-config --modversion smcs':             monoVersion,
    'pkg-config --modversion xsp':              '2.4.2',
}

# These packages are unique to linux
linux_pkgs = {
    'pkg-config --modversion gnome-sharp-2.0':  '2.24.0',
    'pkg-config --modversion mono':             monoVersion,
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
    'pkg-config --modversion mono':             monoVersion,
}


# These executables are common across all platforms
exes = {
    'mono --version':               monoVersion,
    'mcs --version':                monoVersion,
    'gmcs --version':               monoVersion,
    'smcs --version':               monoVersion,
    'xsp --version':                '2.4.2.0',
    'xsp1 --version':               '2.4.2.0',
    'xsp2 --version':               '2.4.2.0',
    'monolinker --version':         '0.2.0.0',
    'resgen --version':             monoVersion,
    'resgen1 --version':            monoVersion,
    'resgen2 --version':            monoVersion,
    'mod-mono-server --version':    '2.4.2.0',
    'mod-mono-server1 --version':   '2.4.2.0',
    'mod-mono-server2 --version':   '2.4.2.0',
    'signcode --version':           monoVersion,
    'csharp --version':             monoVersion,
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
    'fastcgi-mono-server --version':                 '2.4.2.0',
    'fastcgi-mono-server1 --version':                '2.4.2.0',
    'fastcgi-mono-server2 --version':                '2.4.2.0',
    'ipy -V':                                        '1.1',
    'ipy2 -V':                                       '2.0A5',
    'makecert':                                      monoVersion,
    'mdoc --version':                                '0.1.0',
}

# These executables are unique to win32
win32_exes = {
    'envsubst --version':                            '0.17',
    'gconftool-2 --version':                         '2.22.0',
    'gdk-pixbuf-csource --version':                  '2.14.7',
    'glib-genmarshal --version':                     '2.18.4',
    'monodis':                                       'Disassembler',
    'monograph --version':                           '0.2',
    'msgfmt --version':                              '0.17',
    'pango-querymodules --version':                  '1.22.4',
    'pkg-config --version':                          '0.23',
    'recode-sr-latin.exe --version':                 '0.17',
    'booc --version':                                '0.9.1.3287',
    'caspol':                                        monoVersion,
    'certmgr':                                       monoVersion,
    'chktrust':                                      monoVersion,
    'disco':                                         monoVersion,
    'fastcgi-mono-server --version':                 '2.4.2.0',
    'fastcgi-mono-server1 --version':                '2.4.2.0',
    'fastcgi-mono-server2 --version':                '2.4.2.0',
    'gendarme --version':                            '2.4.2.0',
    'ikvm -version':                                 '0.38.0.4',
    'ipy -V':                                        '1.1',
    'ipy2 -V':                                       '2.0A5',
    'makecert':                                      monoVersion,
    'mdoc --version':                                '0.1.0',
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
    'vbnc':                                          '0.0.0.5914',
    'xbuild --version':                              '0.1',
}

# vim:ts=4:expandtab:
