"""Application wrapper for banshee"""

from strongwind import *
import os

def launchBanshee(exe=None):
	if exe is None:
		exe = 'banshee-1'
	args = [exe]
	(app, subproc) = cache.launchApplication(args=args)
	 banshee = GtkBansheeMediaPlayer(app, subproc)
    cache.addApplication(banshee)
    banshee.gtkBansheeMediaPlayerFrame.app = banshee
    return banshee

class GtkBansheeMediaPlayer(accessibles.Application):
    def __init__(self, accessible, subproc=None):
        'Get a reference to the Banshee window'
        super(GtkBansheeMediaPlayer, self).__init__(accessible, subproc)
        self.findFrame("Banshee Media Player")
