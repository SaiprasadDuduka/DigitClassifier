import pygame as pg
import pandas as pd
import sys
import csv
import classifier

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
			pg.display.update()
			
		if state[1]:
			screen.fill((0,0,0))
			pg.display.update()
			
		if state[2]:
			#Store the files in pixel_num.csv file
			with open('D:\\My Projects\\Digit Classifier - ML\\csv\\pixel_num.csv', 'w', newline = '') as f:
				thewriter = csv.writer(f)
				pix_arr = pg.PixelArray(screen)
				
				arr = []
				for col in range(len(pix_arr[0])):
					for row in range(len(pix_arr)):
						if pix_arr[col][row] == screen.map_rgb((255, 255, 255)):
							arr.append('0')
						else:
							arr.append('1')
				
				thewriter.writerow(arr)
				thewriter.writerow(arr)
				f.close()
				del pix_arr
			
			#Use classifier
			classifier.predict()
			ans = pd.read_csv('D:\\My Projects\\Digit Classifier - ML\\csv\\ans.csv').values
			
			#Print Prediction
			screen.fill((0,0,0))
			text = pg.font.Font('freesansbold.ttf', 12)
			predict_num = text.render('Predicted Number: ' + str(ans[0, 0]), True, white)
			predict_rect = predict_num.get_rect()
			predict_rect.center = (64,64)
			screen.blit(predict_num, predict_rect)
			pg.display.update()
				
			
			
			