import pygame as pg

size = [800,600]
pg.init()
screen = pg.display.set_mode(size)

p1 = pg.Rect((size[0]/2,size[1]/2,10,10))

running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
    

    pg.draw.rect(screen,(0,0,200),p1)
    pg.display.update()

pg.quit()