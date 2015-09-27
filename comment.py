import sys
from pyText import *

WHITE = (255, 255, 255)
BLACK = (10, 10, 10)

class comment():
	# The comment itself
	text = ""
	# The coordinates of the comment. X should be constant, y should be in rows
	x = 1000
	y = 20
	live = True
	def __init__(self, text, x, y, font):
		self.text = text
		self.x = x
		self.y = y
		self.comment, self.width = textOutline(font, self.text, WHITE, BLACK)
	
	def getComment(self):
		return self.comment
	
	def scroll(self):
		self.x -= 5
		if self.x < -1 * self.width:
			self.live = False
