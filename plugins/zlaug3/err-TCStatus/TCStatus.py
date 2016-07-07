import json
import socket
import sys
import webbrowser
import requests
import urllib2
import urllib
import xml.etree.ElementTree as ET
import ssl

from BeautifulSoup import BeautifulStoneSoup
from BeautifulSoup import BeautifulSoup
from lxml import html, etree
from errbot import BotPlugin, botcmd
from pyteamcity import TeamCity



class TCStatusBot(BotPlugin):
	"""'TCStatus!' plugin for Errbot"""
	
	s = socket.socket()
	host = ''
	port = ''	
		
	@botcmd	
	def tcstatus(self, msg, args):
		""" Get build status """
		#tc = TeamCity('zlaughery','','http://localhost',89)
		tc = TeamCity('zlaughery','','',89)
		
		buildsUrl = 'http:///httpAuth/app/rest/builds/'
		url = 'http:///viewLog.html?buildId=11&buildTypeId='
		buildInfoUrl = 'http:///httpAuth/app/rest/buildTypes/id:%s/builds/running:false,status:success' % args
		"""
		Uses TeamCity builds list url to parse information straight from the source code.
		Uses the arguments passed (buildTypeID) to select which build.
		Proceeds to take all the information on the page regarding that build
		and spit it back to the user. Along with a couple extra messages. 
		"""
		completeUrl = url + args
		
		page = requests.get(buildInfoUrl, verify=False)
		tree = html.fromstring(page.content)
		#page = urllib2.urlopen(buildInfoUrl, verify=False)
		#tree = etree.fromstring((page.content).replace("&","&amp;"))
		#tree2 = tree.replace("&", "&amp;")
		#results = tree2.xpath('//build[@buildTypeId="testbuild8"]')[0]
		
		#for node in results:
			#buildStatus = node["status"]
			#buildState = node["state"]
		
		#tree = ET.parse(buildInfoUrl)
		#root = tree.getroot()
		#parser = etree.XMLParser(recover=True)
		#tree = ET.fromstring(buildInfoUrl, parser=parser)
		#root = tree.getroot()
		#for child in root:
		#	print child.tag, child.attrib
		ctx = ssl.create_default_context()
		ctx.check_hostname = False
		ctx.verify_mode = ssl.CERT_NONE
		
		#f = urllib2.urlopen(buildInfoUrl, context=ctx)
		#z = f.read()
		#f.close()
		#soup = BeautifulSoup(f)
		
		soup = BeautifulSoup(page.content)
		status = soup.findAll('build')
		print buildInfoUrl
		#print page.content
		#print tree
		print soup
		print status
		print "hi"
		print status
		print "hi"
		print status
		print "hi"
		
		
		"""for build in root.findall('build'):
			state = build.get('state')
			status = build.get('status')
			queDate = build.get('queuedDate')
			startDate = build.get('startDate')
			finishDate = build.get('finishDate')
			trigBy = build.get('name')"""
			
			
		"""
		buildStatus = tree.xpath('//build[@buildTypeId="%s"]' % args)[0]
		buildState = tree.xpath('//build[@state]/text()')
		queDate = tree.xpath('//queuedDate')
		startDate = tree.xpath('//startDate')
		finishDate = tree.xpath('//finishDate')
		trigBy = tree.xpath('//user[@username]/text()')"""
		
		"""
		print 'Here is your build information: '
		print buildStatus
		print '\n'
		print 'Here is a link to the build %s: %s' % (args, completeUrl)"""
		
		return json.dumps(status)
		
