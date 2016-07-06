import json
import socket
import webbrowser


from errbot import BotPlugin, botcmd
from pyteamcity import TeamCity


class TCBuildBot(BotPlugin):
	"""'TCBuild!' plugin for Errbot"""
	
	s = socket.socket()
	host = '127.0.0.1'
	port = 89
		
	@botcmd	
	def tcbuild(self, msg, args):
		""" Trigger build. """
		#tc = TeamCity('zlaughery','zane1234','http://localhost',89)
		tc = TeamCity('zlaughery','zane1234','127.0.0.1',89)
		
		#data = tc.get_project_by_project_id('testproj')
		url = "http://zlaughery:zane1234@127.0.0.1:89/httpAuth/action.html?add2Queue=" + args
		webbrowser.open(url)
		
		#return json.dumps(data, indent=4)
		return "Triggered build: " + args + ".\n Please refer to '!tcstatus [buildID]', or the TeamCity page to check your build status. \n Check '!tclist' to see all queued builds. \n Thanks!"
		
		