import json
import socket
import webbrowser
import requests
import sys

from lxml import html
from errbot import BotPlugin, botcmd
from pyteamcity import TeamCity


class TCListBot(BotPlugin):
	"""'TCList!' plugin for Errbot"""
	
	s = socket.socket()
	host = '127.0.0.1'
	port = 89
	#url = 'http://127.0.0.1:89/viewLog.html?buildId=11&buildTypeId='
	
		
	@botcmd	
	def tclist(self, msg, args):
		""" Get scheduled build list. """
		#tc = TeamCity('zlaughery','zane1234','http://localhost',89)
		tc = TeamCity('zlaughery','zane1234','127.0.0.1',89)
		url = 'http://127.0.0.1:89/queue.html'
		#webbrowser.open(url)
		
		page = requests.get(url, verify=False)
		tree = html.fromstring(page.content)
		
		schedBuilds = tree.xpath('//div[@id=content]/text()')
		"""
		print "Here is a list of queued builds: "
		print schedBuilds
		print "\n"
		print "Here is a link to the build page: %s" % url"""
		
		return 'Here is a list of queued builds: ' + ''.join(schedBuilds) + '\n Here is a link to the build page: ' + url + "\n If you would like to trigger a build, use !tcbuild [buildID]. \n To check the status of a build use !tcstatus [buildID]. \n Thanks for using ChatOps!"
		
		
		