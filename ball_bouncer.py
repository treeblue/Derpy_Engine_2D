import pygame as pg
from module import object, scene
from time import sleep


size = [800,600]
pg.init()
screen = pg.display.set_mode(size)

p1 = object(pos=[size[0]/2,size[1]/2],vel=[10.,0])

frame = scene()
frame.track(p1)


if __name__ == "__main__":
    running = True
else:
    running = False

waiter = False
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
    screen.fill((0,0,0))

    key = pg.key.get_pressed()
    MAGNITUDE = 1.5
    if not waiter:
        if key[pg.K_a] == True:
            p1.push([-MAGNITUDE,0.])
        elif key[pg.K_d] == True:
            p1.push([MAGNITUDE,0.])
        elif key[pg.K_w] == True:
            p1.push([0.,-MAGNITUDE-10])
            waiter = True
        elif key[pg.K_s] == True:
            p1.push([0.,MAGNITUDE])
    else:
        if key[pg.K_w] == False:
            waiter = False

    print(waiter)

    frame.update()
    for obj in frame.objects:
        x,y = obj.get_pos()
        # print(int(x),int(y))
        R = pg.Rect((int(x),int(y),10,10))
        pg.draw.rect(screen,(0,0,200),R)
    pg.display.update()
    sleep(0.05)

pg.quit()