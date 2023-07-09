import pygame as pg
import sys
from pickle import dump 

#---INITIALIZATION------------#
level = 0
LevelList = []
run = True
scroll = -400
click_init = False
new_rect = False
spos = cpos = (0,0)
cRect = pg.Rect(0,0,0,0)

white = '#FFFFFF'

pg.init()
screen = pg.display.set_mode((500,800))
#---LOGIC---------------------#

while run:
	pg.time.Clock().tick()

	for event in pg.event.get():
		if event.type == pg.QUIT:
			pg.quit()
			sys.exit()
		if event.type == pg.KEYDOWN:
			if event.key == pg.K_s:
				run = False
			if event.key == pg.K_z:
				try:
					del LevelList[-1]
				except IndexError:
					pass
		if event.type == pg.MOUSEBUTTONDOWN:
			if event.button == 5:
				scroll = min((scroll+20,-400 ))
			if event.button == 4:
				scroll -=20

			print(scroll)

	screen.fill('black')

	for i in range(1,80):
		pg.draw.line(screen,'#202020',(0,i*10),(500,i*10))
	for i in range(1,50):
		pg.draw.line(screen,'#202020',(i*10,0),(i*10,800))

	if pg.mouse.get_pressed()[0]:
		new_rect = True
		if not click_init:
			spos = (pg.mouse.get_pos()[0] // 10,pg.mouse.get_pos()[1] // 10)
			click_init = True
		cpos = (pg.mouse.get_pos()[0] // 10,pg.mouse.get_pos()[1] // 10)
		cRect = pg.Rect(spos[0]*10,spos[1]*10,-(spos[0]-cpos[0])*10,-(spos[1]-cpos[1])*10)

		pg.draw.rect(screen,'#303030',cRect)
	elif new_rect:
		cRect.y += scroll
		LevelList.append(cRect)
		print(cRect)
		cpos = spos = (0,0)
		cRect = pg.Rect(0,0,0,0)
		new_rect = False
		click_init = False


	for i in LevelList:
		#try:
			rect = i.copy()
			rect.y -= scroll
			pg.draw.rect(screen,white,rect)
		#except TypeError:
			#pass
	pg.display.flip()
#---SAVING--------------------#

with open(f'Levels/Level{level}.dat','wb') as file:
	dump(LevelList,file)
#-----------------------------#

