import pickle
import pygame as pg
import sys
#---INITIALIZATION------------#
level = 0

with open(f'Levels/Level{level}.dat','rb') as file:
	LevelList = pickle.load(file)

pg.init()
screen = pg.display.set_mode((500,800))

#---RENDERING-----------------#
while True:
	pg.time.Clock().tick(60)
	for event in pg.event.get():
			if event.type == pg.QUIT:
				pg.quit()
				sys.exit()

	screen.fill('black')

	for rect in LevelList:
		if rect.midbottom[1] > 0 and rect.midtop[1] < 800:
			pg.draw.rect(screen,'white',rect)
		rect.y+=2

	pg.display.flip()
#-----------------------------#