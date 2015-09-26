'''A simple graphics example constructs a face from basic shapes.
'''

from graphics import *
from threading import Semaphore, Thread

class message():
	# The message itself
	text = ""
	# The coordinates of the message. X should be constant, y should be in rows
	x = 1000
	y = 20
	live = True
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
		self.x -= 1
		if self.x < -500:
			self.message.undraw()
			self.live = False

class chat():
	messages = []
	
	def __init__(self):
		print "Chat logging starting"
	
	def add(self, message):
		self.messages.append(message)
	
	def run(self):
		for message in self.messages:
			message.scroll()
			if not message.live:
				print "Message gone"
				self.messages.remove(message)
	
	def empty(self):
		return len(self.messages) == 0

def aaaaa(sema):
	print "aaaa"
	time.sleep(3)
	print "bbbb"
	sema.release()
	return

def main():
	win = GraphWin('Face', 1000, 500) # give title and dimensions
	
	x = 1000
	#Background
	win.setBackground("Black")
	
	messages = chat()
	
	test = message("This is another comment", 1200, 50)
	test.draw(win)
	
	text = message("This is a comment", 1000, 20)
	text.draw(win)
	
	messages.add(test)
	messages.add(text)
	sema = Semaphore(0)
	t = Thread(target=aaaaa, args=(sema,))
	t.start()
	
	while True:
		#win.getMouse()
		if not messages.empty():
			messages.run()
			time.sleep(.004)
		if messages.empty():
			#sema.acquire()
			asdf = message("asdfasdfa", 1000, 70)
			asdf.draw(win)
			messages.add(asdf)
		if win.isClosed():
			t.join()
			exit()
		
	#win.close()
	#win.promptClose(10, 10)

main()