import pygame
from pygame.locals import *
import sys

pygame.init()

#Can be changed
antiAl = True
fontABC = pygame.font.Font('/Users/austintarango/Desktop/Wyomoto/Xolonium-Bold.otf', 30)
font123 = pygame.font.Font('/Users/austintarango/Desktop/Wyomoto/radiospacecondital.ttf', 100)
font123small = pygame.font.Font('/Users/austintarango/Desktop/Wyomoto/radiospacecondital.ttf', 50)
font123big = pygame.font.Font('/Users/austintarango/Desktop/Wyomoto/radiospacecondital.ttf', 200)
bg = pygame.image.load('/Users/austintarango/Desktop/Wyomoto/bgEdit.png')
satelliteIcon = pygame.image.load('/Users/austintarango/Desktop/Wyomoto/sattel.png')
magdemLogo = pygame.image.load('/Users/austintarango/Desktop/Wyomoto/Logo.png')
speedometerGauge = pygame.image.load('/Users/austintarango/Desktop/Wyomoto/FullCircle/CIRCLES-Standard-BlueGlow1-BigProgress1-0001.png')

#Don't change
widthDis = pygame.display.Info().current_w
heightDis = pygame.display.Info().current_h
size = widthDis, heightDis
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
bg = pygame.transform.scale(bg, (widthDis, heightDis))
magdemLogo = pygame.transform.scale(magdemLogo, (widthDis/4, heightDis/4))
satelliteIcon = pygame.transform.scale(satelliteIcon, (widthDis/20, heightDis/15))
speedometerGauge = pygame.transform.scale(speedometerGauge, (int(widthDis/2.2), int(heightDis/1.65)))



#Objects
speedMPHLabel = fontABC.render('MPH', antiAl, (9,200,255))
nameLabel = font123.render('7220', antiAl, (9,200,255))
hunnyLabel = fontABC.render('HUNNY', antiAl, (9,200,255))

uniTimeLabel = fontABC.render('UTC', antiAl, (9,200,255))

altLabel = fontABC.render('ALT', antiAl, (9,200,255))

def updateDashValues(speed, alt, sat,utc):
	setUpObj()
	if speed >= 100:
		speed = 100
	elif speed <= 0:
		speed = 1

	speedometerGauge = pygame.image.load('/Users/austintarango/Desktop/Wyomoto/FullCircle/CIRCLES-Standard-BlueGlow1-BigProgress1-0' + "%03d"%(speed*4) +  '.png')
	print '/Users/austintarango/Desktop/Wyomoto/FullCircle/CIRCLES-Standard-BlueGlow1-BigProgress1-0' + "%03d"%speed +  '.png'

	speedMPH = font123big.render("%01d"%speed, antiAl, (9,200,255))
	satelliteNum = font123.render("%01d"%sat, antiAl, (9,200,255))
	uniTimeNum = font123small.render(str(utc), antiAl, (9,200,255))
	altNum = font123small.render(str(alt), antiAl, (9,200,255))


	speedometerGauge = pygame.transform.scale(speedometerGauge, (int(widthDis/2.2), int(heightDis/1.65)))
	screen.blit(speedometerGauge, [widthDis/1.87,heightDis/20])
	screen.blit(satelliteNum, [widthDis/1.4, heightDis/1.5])
	screen.blit(uniTimeNum, [widthDis/10, heightDis/1.43])
	screen.blit(altNum, [widthDis/2.95, heightDis/2.17])
	screen.blit(speedMPH, [widthDis/1.5,heightDis/5])


speed=1
alt=7220
utc=283745
sat=2

def setUpObj():
	screen.blit(bg, [0, 0])
	screen.blit(magdemLogo, [widthDis/3, heightDis/1.3])
	screen.blit(satelliteIcon, [widthDis/1.35, heightDis/1.23])
	screen.blit(uniTimeLabel, [widthDis/7.8, heightDis/1.2])
	screen.blit(altLabel, [widthDis/2.67, heightDis/1.65])
	screen.blit(nameLabel, [widthDis/20,heightDis/5])
	screen.blit(hunnyLabel, [widthDis/8,heightDis/3])
	screen.blit(speedMPHLabel, [widthDis/1.38,heightDis/2.1])

setUpObj()


while 1:

	for event in pygame.event.get():
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_ESCAPE:
				pygame.display.quit()
				pygame.quit()
				sys.exit()
			if event.key == pygame.K_z:
				speed = speed + 1
				alt = alt + 100000
				utc = utc + 100000
				sat = sat + 1
				updateDashValues(speed, alt, sat, utc)
			if event.key == pygame.K_x:
				speed = speed - 1
				alt = alt - 100000
				utc = utc - 100000
				sat = sat - 1
				updateDashValues(speed, alt, sat, utc)

	pygame.display.flip()

