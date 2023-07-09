
import pygame

class TxButton():
	def __init__(self, x, y, txt, color, font, size):
		font = pygame.font.SysFont(font,size)
		self.label = font.render(txt, True, color)
		self.rect = self.label.get_rect(center = (x,y))
		self.clicked = False
	
	def update(self,surface,pos):
		action  = False
		if self.rect.collidepoint(pos):
			action = True
		surface.blit(self.label,self.rect)
		return action
