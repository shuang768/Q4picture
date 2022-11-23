import pygame, sys
from pygame.locals import QUIT
from pygame import Color, Rect
from pygame import draw
from pygame import display

pygame.init()
gameDisplay = display.set_mode((800,800))
gameDisplay.fill(Color('lightblue'))
draw.rect(gameDisplay, Color('brown'), Rect(150, 300, 300, 200))
draw.rect(gameDisplay, Color('grey'), Rect(350, 165, 50, 100))
draw.polygon(gameDisplay, Color('black'), [(150, 300), (450, 300), (300, 150)])
draw.ellipse(gameDisplay, Color('yellow'), Rect(100, 20, 100, 100))
draw.rect(gameDisplay, Color('red'), Rect(250, 400, 65, 100))
draw.circle(gameDisplay, Color('black'), (265, 450), 5)
draw.circle(gameDisplay, Color('white'), (450, 110), 50)
draw.circle(gameDisplay, Color('white'), (375, 110), 50)
draw.rect(gameDisplay, Color('red'), Rect(175, 325, 50, 50))
draw.rect(gameDisplay, Color('red'), Rect(350, 325, 50, 50))
draw.polygon(gameDisplay, Color('green'), [(0, 550), (20, 550), (10, 525)])
n=0
for i in range (1,40):
  n=n+15
  m=n+20
  o=n+10
  draw.polygon(gameDisplay, Color('green'), [(n, 550), (m, 550), (o, 525)])
draw.polygon(gameDisplay, Color('green'), [(5, 570), (25, 570), (15, 545)])
draw.polygon(gameDisplay, Color('green'), [(0, 570), (20, 570), (10, 545)])
n=5
for i in range (1,40):
  n=n+15
  m=n+20
  o=n+10
  draw.polygon(gameDisplay, Color('green'), [(n, 570), (m, 570), (o, 545)])
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()