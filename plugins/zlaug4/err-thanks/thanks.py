import re

from errbot import BotPlugin, botcmd


class ThanksBot(BotPlugin):
	"""'Thanks!' plugin for Errbot"""
	
	
	@botcmd
	def thanks(self, msg, args):
		"""Say you're welcome to someone"""
		userOrig = format(msg.frm)
		user = re.split('@|/',userOrig)
		return "You are very welcome, " + ''.join(user[1]) + "!"