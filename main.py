import pygame as pg
import sys
import buttons
from pickle import load

#---INITIALIZATION------------#
pg.init()
screen = pg.display.set_mode((500,800),pg.DOUBLEBUF)
pg.mixer.init()
music = pg.mixer.Sound('theme.wav')
musicPlaying = False

level = 2


#---FUNCTIONS-------------------#
def main():
	bgcolor = '#f0f0f0'
	OBSTCOLOR = '#606060'
	BALLCOLOR = '#ff3300'
	player = [0,0,True]
	player[0],player[1] = (250,700)
	paused = False
	started = False
	mainmenu = buttons.TxButton(250,300,'Main Menu','#606060','American Typewriter',50)
	quit = buttons.TxButton(250,400,'Quit','#606060','American Typewriter',50)

	with open(f'Levels/Level{level}.dat','rb') as file:
		LevelList = load(file)
	#speed = 1
	counter = 0
	secs = 0
	while True:
		if not paused: counter+=1
		if counter == 60:
			secs += 1
			counter = 0
		#speed = 1+(secs/30)

		c = (player[0],player[1])
		r = 20
		Points = [

			(c[0]+r,c[1]),
			(c[0]-r,c[1]),
			(c[0],c[1]+r),
			(c[0],c[1]-r),

			(c[0]+((5*(r**2)/9)**0.5),c[1]+2*r/3),
			(c[0]+((8*(r**2)/9)**0.5),c[1]+r/3),
			(c[0]-((5*(r**2)/9)**0.5),c[1]+2*r/3),
			(c[0]-((8*(r**2)/9)**0.5),c[1]+r/3),
			(c[0]-(((r**2)/9)**0.5),c[1]+2.75*r/3),
			(c[0]+(((r**2)/9)**0.5),c[1]+2.75*r/3),

			(c[0]+((5*(r**2)/9)**0.5),c[1]-2*r/3),
			(c[0]+((8*(r**2)/9)**0.5),c[1]-r/3),
			(c[0]-((5*(r**2)/9)**0.5),c[1]-2*r/3),
			(c[0]-((8*(r**2)/9)**0.5),c[1]-r/3),
			(c[0]-(((r**2)/9)**0.5),c[1]-2.75*r/3),
			(c[0]+(((r**2)/9)**0.5),c[1]-2.75*r/3)
			
		]
		mouseposcheck = (0,0)
		for event in pg.event.get():
			if event.type == pg.QUIT:
				pg.quit()
				sys.exit()
			if event.type == pg.KEYDOWN:
				if event.key == pg.K_ESCAPE:
					if paused: paused = False
					else: paused = True
				if event.key == pg.K_SPACE:
					if not started:started = True
					if player[2]:
						player[2] = False
					else:
						player[2] = True

			if event.type == pg.MOUSEBUTTONDOWN:
				mouseposcheck = event.pos

		pg.time.Clock().tick(60)
		screen.fill(bgcolor)
		if paused:
			if mainmenu.update(screen,mouseposcheck):
				return menu
			if quit.update(screen,mouseposcheck):
					pg.quit()
					sys.exit()
		else:

			for rect in LevelList:
				if rect.midbottom[1] > 0 and rect.midtop[1] < 800:
					pg.draw.rect(screen,OBSTCOLOR,rect)
					for point in Points:
						if rect.collidepoint(point):
							return death
				if started:rect.y+=2

			if player[0]+20 >= 499:
				player[2] = False
			elif player[0]-20 <= 1:
				player[2] = True

			if started:
				if player[2]:
					player[0] += 3
				else:
					player[0] -= 3



			pg.draw.circle(screen,BALLCOLOR,(player[0],player[1]),r)
			
			time = pg.font.SysFont('American Typewriter',50).render(f'{secs}',True,'#ff3300')
			time_rect = time.get_rect(topright = (500,0))
			screen.blit(time,time_rect)



		pg.display.flip()

def menu():
	
	font = pg.font.SysFont('Daddy Longlegs NF',200)
	playBttn = buttons.TxButton(250,500,'Play','#606060','American Typewriter',50)
	sttnBttn = buttons.TxButton(250,600,'Settings','#606060','American Typewriter',50)
	quitBttn = buttons.TxButton(250,700,'Quit','#606060','American Typewriter',50)


	while True:
		mouseposcheck = (0,0)
		for event in pg.event.get():
			if event.type == pg.QUIT:
				pg.quit()
				sys.exit()
			if event.type == pg.MOUSEBUTTONDOWN:
				mouseposcheck = event.pos

		pg.time.Clock().tick(60)
		screen.fill('#f0f0f0')
		label = font.render('Teflon',True,'#606060')
		label_rect = label.get_rect(center = (250,200))

		if playBttn.update(screen,mouseposcheck):
			return main
		if sttnBttn.update(screen,mouseposcheck):
			return Settings
		if quitBttn.update(screen,mouseposcheck):
			pg.quit()
			sys.exit()

		screen.blit(label,label_rect)
		pg.display.flip()

def Settings():
	
	global musicPlaying,music
	MenuBttn = buttons.TxButton(250,500,'Menu','#606060','American Typewriter',50)
	MsicBttn = buttons.TxButton(250,400,'Music','#606060','American Typewriter',50)
	
	while True:
		mouseposcheck = (0,0)
		for event in pg.event.get():
			if event.type == pg.QUIT:
				pg.quit()
				sys.exit()
			if event.type == pg.MOUSEBUTTONDOWN:
				mouseposcheck = event.pos

		pg.time.Clock().tick(60)
		
		screen.fill('#f0f0f0')
		
		if MsicBttn.update(screen,mouseposcheck):
			if musicPlaying == True:
				musicPlaying = False
				music.stop()
			elif musicPlaying == False:
				musicPlaying = True
				music.play()
		if MenuBttn.update(screen,mouseposcheck):
			return menu


		pg.display.flip()

def death():

	txt = ('Youre Dead','TRy level {} again?'.format(level))
	font = pg.font.SysFont('Daddy Longlegs NF',200)
	tryAgain = buttons.TxButton(250,500,'Try Again','#606060','American Typewriter',50)
	mainMenu = buttons.TxButton(250,700,'Menu','#606060','American Typewriter',50)
	while True:
		mouseposcheck = (0,0)
		for event in pg.event.get():
			if event.type == pg.QUIT:
				pg.quit()
				sys.exit()
			if event.type == pg.MOUSEBUTTONDOWN:
				mouseposcheck = event.pos

		pg.time.Clock().tick(60)
		screen.fill('#f0f0f0')
		if mainMenu.update(screen,mouseposcheck):
			return menu
		if tryAgain.update(screen,mouseposcheck):
			return main
		
		pg.display.flip()


func = menu
if __name__ == '__main__':
	while True:
		func = func()