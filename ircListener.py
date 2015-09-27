# twisted imports
from twisted.words.protocols import irc
from twisted.internet import reactor, protocol
from twisted.python import log

# system imports
import time, sys

class TwitchMonitor(irc.IRCClient):
	"""Client to monitor Twitch chat"""
	
	nickname = "justinfan31415926535"
	
	def connectionMade(self):
		irc.IRCClient.connectionMade(self)

	def connectionLost(self, reason):
		irc.IRCClient.connectionLost(self, reason)


	# callbacks for events

	def signedOn(self):
		"""Called when client has succesfully signed on to server."""
		self.join(self.factory.channel)

	def privmsg(self, user, channel, msg):
		"""This will get called when the client receives a message."""
		user = user.split('!', 1)[0]
		print("<%s> %s" % (user, msg))

	def action(self, user, channel, msg):
		"""This will get called when the client sees someone do an action."""
		user = user.split('!', 1)[0]
		print("* %s %s" % (user, msg))



class MonitorFactory(protocol.ClientFactory):
	"""A factory for TwitchMonitor.

	A new protocol instance will be created each time we connect to the server.
	"""

	def __init__(self, channel):
		self.channel = channel

	def buildProtocol(self, addr):
		p = TwitchMonitor()
		p.factory = self
		return p

	def clientConnectionLost(self, connector, reason):
		"""If we get disconnected, reconnect to server."""
		connector.connect()

	def clientConnectionFailed(self, connector, reason):
		print "connection failed:", reason
		reactor.stop()


if __name__ == '__main__':
	
	# create factory protocol and application
	f = MonitorFactory(sys.argv[1])

	# connect factory to this host and port
	reactor.connectTCP("irc.twitch.tv", 6667, f)

	# run bot
	reactor.run()