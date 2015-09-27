from comment import comment
from random import randint
class chat():
	comments = []
	i = 0
	
	def __init__(self, font):
		self.font = font
		print "Chat logging starting"
	
	def addComment(self, msg):
		#row = randint(0, 20) * 25
		comm = comment(msg, 1184, self.i*25, self.font)
		self.i += 1
		if self.i >= 20:
			self.i = 0
		#print "Added comment: " + msg
		self.comments.append(comm)
	
	def run(self):
		for comm in self.comments:
			comm.scroll()
			if not comm.live:
				#print "Comment gone"
				self.comments.remove(comm)
	
	def empty(self):
		return len(self.comments) == 0
