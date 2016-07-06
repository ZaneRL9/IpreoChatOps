import re

from errbot import BotPlugin, botcmd


class HelloBot(BotPlugin):
	"""'Hello!' plugin for Errbot"""
	
	
	@botcmd
	def hello(self, msg, args):
		"""Say hello to someone"""
		userOrig = format(msg.frm)
		user = re.split('@|/',userOrig)
		return "Hello, " + ''.join(user[1]) + "!"