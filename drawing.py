'''A simple graphics example constructs a face from basic shapes.
'''

from graphics import *

class message():
	# The message itself
	text = ""
	# The coordinates of the message. X should be constant, y should be in rows
	x = 1000
	y = 20
	def __init__(self, text, x, y):
		self.text = text
		self.x = x
		self.y = y
		self.message = Text(Point(self.x, self.y), text)
		self.message.setFace('helvetica')
		self.message.setStyle('bold')
		self.message.setFill('White')
		self.message.setSize(20)
	
	def draw(self, win):
		self.message.draw(win)
	
	def scroll(self):
		self.message.move(-2, 0)

def main():
	win = GraphWin('Face', 1000, 500) # give title and dimensions
	
	x = 1000
	#Background
	win.setBackground("Black")
	
	test = message("This is a blowup", 1200, 50)
	test.draw(win)
	
	text = message("This is a test", 1000, 20)
	text.draw(win)
	
	
	
	while True:
		#win.getMouse()
		text.scroll()
		test.scroll()
		time.sleep(.005)
		if win.isClosed():
			return
		
	#win.close()
	#win.promptClose(10, 10)

main()