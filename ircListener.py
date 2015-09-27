# twisted imports
from twisted.words.protocols import irc
from twisted.internet import reactor, protocol
from twisted.python import log

# system imports
import time, sys
from chat import chat
from comment import comment
from threading import Thread
import pygame

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
		#print("<%s> %s" % (user, msg))
		self.twitch.addComment(msg)

	def action(self, user, channel, msg):
		"""This will get called when the client sees someone do an action."""
		user = user.split('!', 1)[0]
		#print("* %s %s" % (user, msg))
		self.twitch.addComment(msg)



class MonitorFactory(protocol.ClientFactory):
	"""A factory for TwitchMonitor.

	A new protocol instance will be created each time we connect to the server.
	"""

	def __init__(self, channel, twitchChat):
		self.channel = channel
		self.twitch = twitchChat

	def buildProtocol(self, addr):
		p = TwitchMonitor()
		p.factory = self
		p.twitch = self.twitch
		return p

	def clientConnectionLost(self, connector, reason):
		"""If we get disconnected, reconnect to server."""
		connector.connect()

	def clientConnectionFailed(self, connector, reason):
		print "connection failed:", reason
		reactor.stop()


def runReactor(reactor):
	reactor.run()
	return

if __name__ == '__main__':
	
	pygame.init()
	twitchFont = pygame.font.SysFont("helvetica", 24, bold=True)
	twitchChat = chat(twitchFont)
	# create factory protocol and application
	f = MonitorFactory(sys.argv[1], twitchChat)

	# connect factory to this host and port
	reactor.connectTCP("irc.twitch.tv", 6667, f)

	# run bot
	reactorThread = Thread(target=runReactor, args=(reactor,))
	reactorThread.daemon = True
	reactorThread.start()
	#reactor.run()
		
	# Set the height and width of the screen
	SIZE = [1184, 500]
	 
	screen = pygame.display.set_mode(SIZE)
	pygame.display.set_caption("Twitch Chat")
	clock = pygame.time.Clock()
	 
	# Loop until the user clicks the close button.
	GREEN = [00, 100, 0]
	done = False
	while not done:
		for event in pygame.event.get():   # User did something
			if event.type == pygame.QUIT:  # If user clicked close
				done = True   # Flag that we are done so we exit this loop
		
		# Set the screen background
		screen.fill(GREEN)
		
		# Draw words
		for comment in twitchChat.comments:
			screen.blit(comment.getComment(), (comment.x, comment.y))
		
		twitchChat.run()
		
		# Go ahead and update the screen with what we've drawn.
		pygame.display.flip()
		clock.tick(60)
	 
	# Be IDLE friendly. If you forget this line, the program will 'hang'
	# on exit.
	pygame.quit()