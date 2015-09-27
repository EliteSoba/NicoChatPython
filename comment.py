from graphics import *
from Tkinter import TclError
import sys

class comment():
	# The comment itself
	text = ""
	# The coordinates of the comment. X should be constant, y should be in rows
	x = 1000
	y = 20
	live = True
	def __init__(self, text, x, y):
		self.text = text
		self.x = x
		self.y = y
		self.comment = Text(Point(self.x, self.y), text)
		self.comment.setFace('helvetica')
		self.comment.setStyle('bold')
		self.comment.setTextColor('White')
		self.comment.setSize(20)
	
	def draw(self, win):
		self.comment.draw(win)
		
	def undraw(self):
		self.comment.undraw()
	
	def scroll(self):
		try:
			self.comment.move(-2, 0)
		except TclError as e:
			print "I have no idea"
			print "Message: " + self.text
			print "Some error: " + e.message
			print "The args: " + str(e.args)
			print sys.exc_info()[0]
			self.live = False
		self.x -= 1
		if self.x < -50:
			#self.comment.undraw()
			self.live = False
