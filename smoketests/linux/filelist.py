
dirs = [
    '/usr/lib/mono',
    '/etc',

]

files = [

    '/usr/bin/mono',
]

symlinks = [
    '/usr/lib/mono/2.0/System.dll',
]

unexpectedfiles = [
    '/usr/bin/BADFILE',
    '/etc/asdf',
]

unexpecteddirs = [
    '/usr/bin/mono',
    '/usr/bin/mono_ASDF',
]

unexpectedsymlinks = [
    '/usr/bin/mono_BADLINK',
]
