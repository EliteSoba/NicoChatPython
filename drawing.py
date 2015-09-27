'''A simple graphics example constructs a face from basic shapes.
'''

from graphics import *
from threading import Semaphore, Thread
from comment import comment
from chat import chat

def bbbbb(comments):
	while True:
		comments.run()
		time.sleep(.004)
	exit()
	return
def main():
	win = GraphWin('Face', 1000, 500) # give title and dimensions
	
	x = 1000
	#Background
	win.setBackground("Black")
	
	comments = chat(win)
	
	test = comment("This is another comment", 1200, 50)
	words = "This is a commentaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb"
	text = comment(words, 1000+8*len(words), 20)
	
	#comments.add(test)
	comments.add(text)
	sema = Semaphore(0)
	t = Thread(target=bbbbb, args=(comments,))
	t.daemon = True
	t.start()
	
	while True:
		try:
			#words = raw_input()
			#comm = comment(words, 1000, 20)
			#comments.add(comm)
			win.getMouse()
			#comments.run()
			if win.isClosed():
				exit()
		except:
			return
		"""if not comments.empty():
			comments.run()
			time.sleep(.004)
		if comments.empty():
			#sema.acquire()
			asdf = comment("asdfasdfa", 1000, 70)
			asdf.draw(win)
			comments.add(asdf)
		if win.isClosed():
			exit()"""
	
	#win.close()
	#win.promptClose(10, 10)

main()