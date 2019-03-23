import pygame as pg
import sys
import csv

pg.init()
screen = pg.display.set_mode((128,128))
screen.fill((0, 0, 0))
pg.display.set_caption('Digit Classifier')
clock = pg.time.Clock()
z = 0

while True:
	pg.init()
	clock.tick(180)
	white = (255, 255, 255)
	x, y = pg.mouse.get_pos()
	
	#Event Handling
	for event in pg.event.get():
		if event.type == pg.QUIT:
			pg.quit()
			pg.exit
		elif event.type == pg.MOUSEBUTTONDOWN:
			z = 1
		elif event.type == pg.MOUSEBUTTONUP:
			z = 0
			
		state = pg.mouse.get_pressed()
		if z == 1 and state[0]:
			pg.draw.rect(screen,white,pg.Rect((x, y),(10,10)))
			
		if state[1]:
			screen.fill((0,0,0))
			
		if state[2]:
			#Store the files in dataset.csv file
			with open('D:\\My Projects\\Digit Classifier - ML\\csv\\dataset.csv', 'a', newline = '') as f:
				thewriter = csv.writer(f)
				pix_arr = pg.PixelArray(screen)
				
				num = input("Enter number: ")
				pix_row = [num]
				for col in range(len(pix_arr[0])):
					for row in range(len(pix_arr)):
						if pix_arr[col][row] == screen.map_rgb((255, 255, 255)):
							pix_row.append('0')
						else:
							pix_row.append('1')
				
				thewriter.writerow(pix_row)
				f.close()
				del pix_arr
			
			
		pg.display.update()
				
			
			
			