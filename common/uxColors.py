colors = {
        'norm':'\033[0m',
        'red':'\033[31m',
        'green':'\033[32m',
        'orange':'\033[33m',
        'blue':'\033[34m',
        'purple':'\033[35m',
}

def printColor(msg,color):
    print '%s%s%s' % (colors[color],msg,colors['norm'])
