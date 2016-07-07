import json
import socket
import webbrowser


from errbot import BotPlugin, botcmd
from pyteamcity import TeamCity


class TCBuildBot(BotPlugin):
	"""'TCBuild!' plugin for Errbot"""
	
	s = socket.socket()
	host = ''
	port = ''
		
	@botcmd	
	def tcbuild(self, msg, args):
		""" Trigger build. """
		#tc = TeamCity('zlaughery','','http://localhost',port)
		tc = TeamCity('zlaughery','','',port)
		
		#data = tc.get_project_by_project_id('testproj')
		url = "http://zlaughery:password@hostname:port/httpAuth/action.html?add2Queue=" + args
		webbrowser.open(url)
		
		#return json.dumps(data, indent=4)
		return "Triggered build: " + args + ".\n Please refer to '!tcstatus [buildID]', or the TeamCity page to check your build status. \n Check '!tclist' to see all queued builds. \n Thanks!"
		
		
