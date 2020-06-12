import pygame
import pygame_gui
import random
import sys

pygame.init()

#GAME presets
GAMEWIDTH = "1600"
GAMEHEIGHT = "900"
tick = "0"
noDiagonals = "False"
cubeSize = "10"
step = "3"
stepsAtOnce = "1"
fade = "0.1"
heads = "False"
clock = pygame.time.Clock()

#GUI 
GUIWIDTH = 550
GUIHEIGHT = 500
GUIBACKGROUND = '#000000'
guiclock = pygame.time.Clock()

while True:

	gui_is_running = True

	window_surface = pygame.display.set_mode((GUIWIDTH, GUIHEIGHT))
	pygame.display.set_caption('GUI')
	background = pygame.Surface((GUIWIDTH, GUIHEIGHT))
	background.fill(pygame.Color(GUIBACKGROUND))
	manager = pygame_gui.UIManager((GUIWIDTH, GUIHEIGHT))

	label1 = pygame_gui.elements.UILabel(relative_rect=pygame.Rect(50, 10, 200, 25),text='Resolution: ',manager=manager)
	input1_1 = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect(300, 10, 90, 25),manager=manager)
	input1_2 = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect(410, 10, 90, 25),manager=manager)
	input1_1.set_text(GAMEWIDTH)
	input1_2.set_text(GAMEHEIGHT)
	label2 = pygame_gui.elements.UILabel(relative_rect=pygame.Rect(50, 60, 200, 25),text='tick speed: ',manager=manager)
	input2 = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect(300, 60, 200, 25),manager=manager)
	input2.set_text(tick)
	label3 = pygame_gui.elements.UILabel(relative_rect=pygame.Rect(50, 110, 200, 25),text='no diagonals: ',manager=manager)
	input3 = pygame_gui.elements.UIButton(relative_rect=pygame.Rect(300, 110, 200, 25),text=noDiagonals,manager=manager)
	label4 = pygame_gui.elements.UILabel(relative_rect=pygame.Rect(50, 160, 200, 25),text='cube size: ',manager=manager)
	input4 = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect(300, 160, 200, 25),manager=manager)
	input4.set_text(cubeSize)
	label5 = pygame_gui.elements.UILabel(relative_rect=pygame.Rect(50, 210, 200, 25),text='step size: ',manager=manager)
	input5 = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect(300, 210, 200, 25),manager=manager)
	input5.set_text(step)
	label6 = pygame_gui.elements.UILabel(relative_rect=pygame.Rect(50, 260, 200, 25),text='steps at once: ',manager=manager)
	input6 = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect(300, 260, 200, 25),manager=manager)
	input6.set_text(stepsAtOnce)
	label7 = pygame_gui.elements.UILabel(relative_rect=pygame.Rect(50, 310, 200, 25),text='fading: ',manager=manager)
	input7 = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect(300, 310, 200, 25),manager=manager)
	input7.set_text(fade)

	label8 = pygame_gui.elements.UILabel(relative_rect=pygame.Rect(50, 360, 200, 25),text='show heads: ',manager=manager)
	input8 = pygame_gui.elements.UIButton(relative_rect=pygame.Rect(300, 360, 200, 25),text=heads,manager=manager)

	start_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect(225, 420, 100, 50),text='Start',manager=manager)

	while gui_is_running:
	    for event in pygame.event.get():
	        if event.type == pygame.QUIT:
	            sys.exit()

	        if event.type == pygame.USEREVENT:
	            if event.user_type == 'ui_button_pressed':
	            	if event.ui_element == input3:
	            		if input3.text == 'True':
	            			input3.set_text("False")
	            		else:
	            			input3.set_text("True")

	            	if event.ui_element == input8:
	            		if input8.text == 'True':
	            			input8.set_text("False")
	            		else:
	            			input8.set_text("True")

	            	if event.ui_element == start_button and int(input1_1.text)/int(input4.text)>=1 and int(input1_2.text)/int(input4.text)>=1:
	                	gui_is_running = False

	                	GAMEWIDTH = input1_1.text
	                	GAMEHEIGHT = input1_2.text
	                	tick = input2.text
	                	noDiagonals = input3.text
	                	cubeSize = input4.text
	                	step = input5.text
	                	stepsAtOnce = input6.text
	                	fade = input7.text
	                	heads = input8.text


	        manager.process_events(event)

	    manager.update(guiclock.tick(0))
	    window_surface.blit(background, (0, 0))
	    manager.draw_ui(window_surface)
	    pygame.display.update()


	game_runs = True

	pygame.display.set_caption('GAME')
	gameScreen = pygame.display.set_mode((int(GAMEWIDTH),int(GAMEHEIGHT)))
	Nx = int(int(GAMEWIDTH)/int(cubeSize))
	Ny = int(int(GAMEHEIGHT)/int(cubeSize))
	grid = [[0 for x in range(Ny)] for y in range(Nx)]
	x = 0
	y = 0
	hold = False

	while game_runs:

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()

			if event.type == pygame.KEYDOWN:
				if event.key == 27:#ESCAPE
					game_runs = False
				if event.key == 32:#SPACE
					if hold:
						hold = False
					else:
						hold = True
						
		if not hold:

			for a in range(0, len(grid)):
				for b in range (0, len(grid[0])):
					if grid[a][b] > 0:
						grid[a][b] -= float(fade)*int(stepsAtOnce)

			if noDiagonals == "True":

				for n in range(int(stepsAtOnce)):
					if random.randint(0, 1) == 0:
						xdone = False
						while not xdone:
							x1 = x + random.randint(-int(step), int(step))
							if x1 < Nx and x1 >= 0 and x1 != x:
								x = x1
								xdone = True

					else:
						ydone = False
						while not ydone:
							y1 = y + random.randint(-int(step), int(step))
							if y1 < Ny and y1 >= 0 and y1 != y:
								y = y1
								ydone = True	

					grid[x][y] = 767

			else:

				for n in range(int(stepsAtOnce)):
					xdone = False
					ydone = False
					while not xdone:
						x1 = x + random.randint(-int(step), int(step))
						if x1 < Nx and x1 >= 0 and x1 != x:
							x = x1
							xdone = True

					while not ydone:
						y1 = y + random.randint(-int(step), int(step))
						if y1 < Ny and y1 >= 0 and y1 != y:
							y = y1
							ydone = True		

					grid[x][y] = 767
			
			for a in range(0, len(grid)):
				for b in range (0, len(grid[0])):
					if grid[a][b] != 0:

						if grid[a][b] == 767 and heads == "True":
							red = 255
							green = 255
							blue = 255
						elif grid[a][b] >= 512:
							red = grid[a][b] - 512
							green = 255 - red
							blue = 0
						elif grid[a][b] >= 256:
							red = 0
							green = grid[a][b] - 256
							blue = 255 - green
						elif grid[a][b] > 0:
							red = 0
							green = 0
							blue = grid[a][b]
						else:
							red = 0
							green = 0
							blue = 0	

						rgb = (int(red),int(green),int(blue))
						pygame.draw.rect( gameScreen, rgb, (a*int(cubeSize), b*int(cubeSize), int(cubeSize), int(cubeSize)))

			clock.tick(int(tick))
			pygame.display.update()	