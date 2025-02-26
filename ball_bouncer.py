import pygame as pg
from module import object, scene
from time import sleep


size = [800,600]
pg.init()
screen = pg.display.set_mode(size)

blob = object(pos=[size[0]/2,size[1]/2],vel=[10.,0])

frame = scene()
frame.track(blob)


running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
    screen.fill((0,0,0))

    frame.update()
    for obj in frame.objects:
        x,y = obj.get_pos()
        print(x,y)
        R = pg.Rect((int(x),int(y),5,5))
        pg.draw.rect(screen,(0,0,200),R)
    pg.display.update()
    sleep(0.05)

pg.quit()