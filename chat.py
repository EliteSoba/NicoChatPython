from graphics import *
from comment import comment
from random import randint
from threading import Lock

class chat():
	comments = []
	lock = Lock()
	
	def __init__(self, win):
		print "Chat logging starting"
		self.win = win
	
	def addComment(self, msg):
		comm = comment(msg, 1184 + 8 * len(msg), randint(1, 8) * 50)
		self.lock.acquire()
		self.comments.append(comm)
		self.lock.release()
		comm.draw(self.win)
	
	def add(self, comm):
		"""Deprecated"""
		self.comments.append(comm)
		comm.draw(self.win)
	
	def run(self):
		self.lock.acquire()
		for comm in self.comments:
			comm.scroll()
			if not comm.live:
				#print "Comment gone"
				comm.undraw()
				self.comments.remove(comm)
		self.lock.release()
	
	def empty(self):
		return len(self.comments) == 0