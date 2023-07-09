import pygame as pg
import pickle

rect = pg.Rect

LevelList = [
	rect(10, 360, 140, 30),
	rect(350, 360, 140, 30),
    rect(160, 220, 180, 30),
    rect(10, 70, 140, 30),
    rect(350, 70, 140, 30),
    rect(10, 100, 30, 260),
    rect(460, 100, 30, 260),
    
    rect(160, 510-580, 180, 30),
    rect(10, 650-(580+290), 140, 30),
    rect(350, 650-(580+290), 140, 30),
    rect(10, 390-580, 30, 260),
    rect(460, 390-580, 30, 260)]
	
with open(f'Levels/Level{0}.dat','wb') as file:
	#LevelList = 
	pickle.dump(LevelList,file)
	
print(LevelList)