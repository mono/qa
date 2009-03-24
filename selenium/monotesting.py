# This file must exist with these  variables set
#
# rc_host='http://c4193.mono.lab.novell.com:8080'
# rc_server='localhost'
# rc_port=4444
# rc_browser='*chrome'

base_url = 'http://mono-mac1.provo.novell.com'

rc_server = 'localhost'
rc_port = 4444
rc_browser = '*chrome'

xsp1_port = 8081
xsp2_port = 8082
graffiti_port = 8083

xsp1_url = '%s:%d' % (base_url,xsp1_port)
xsp2_url = '%s:%d' % (base_url,xsp2_port)
graffiti_url = '%s:%d' % (base_url,graffiti_port)


