from comment import comment
from random import randint
class chat():
	comments = []
	
	def __init__(self, font):
		self.font = font
		print "Chat logging starting"
	
	def addComment(self, msg):
		comm = comment(msg, 1184, randint(1, 8) * 50, self.font)
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
