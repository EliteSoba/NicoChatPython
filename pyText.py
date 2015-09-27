#!/usr/bin/env python

"""
Outlined text, courtesy of Pete Shinners
http://www.pygame.org/pcr/hollow_outline/index.php

Adapted to return a tuple of the image and the width because of laziness
"""

import os, sys, pygame, pygame.font, pygame.image
from pygame.locals import *

def textHollow(font, message, fontcolor):
	notcolor = [c^0xFF for c in fontcolor]
	base = font.render(message, 0, fontcolor, notcolor)
	size = base.get_width() + 2, base.get_height() + 2
	img = pygame.Surface(size, 16)
	img.fill(notcolor)
	base.set_colorkey(0)
	img.blit(base, (0, 0))
	img.blit(base, (2, 0))
	img.blit(base, (0, 2))
	img.blit(base, (2, 2))
	base.set_colorkey(0)
	base.set_palette_at(1, notcolor)
	img.blit(base, (1, 1))
	img.set_colorkey(notcolor)
	return img, base.get_width() + 2
	
def textOutline(font, message, fontcolor, outlinecolor):
	base = font.render(message, 0, fontcolor)
	outline, width = textHollow(font, message, outlinecolor)
	img = pygame.Surface(outline.get_size(), 16)
	img.blit(base, (1, 1))
	img.blit(outline, (0, 0))
	img.set_colorkey(0)
	return img, width