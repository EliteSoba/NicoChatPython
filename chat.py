from graphics import *

class chat():
	comments = []
	
	def __init__(self, win):
		print "Chat logging starting"
		self.win = win
	
	def add(self, comment):
		self.comments.append(comment)
		comment.draw(self.win)
	
	def run(self):
		for comment in self.comments:
			comment.scroll()
			if not comment.live:
				print "Comment gone"
				self.comments.remove(comment)
	
	def empty(self):
		return len(self.comments) == 0