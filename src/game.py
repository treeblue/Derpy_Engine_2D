import pygame as pg
from time import sleep

class rendering:
    def __init__(self, size:list=[500,500], fps:float=30.) -> None:
        pg.init()
        self.screen = pg.display.set_mode(size)
        self.running = True
        self.frametime = 1/fps

    def end_condition(self) -> bool:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.running = False
        return self.running

    def render_item(self, location:tuple, size:float, colour:tuple=(0,0,200)) -> None:
        R = pg.Rect((location[0],location[1],size,size))
        pg.draw.rect(self.screen,colour,R)

    def loop(self) -> None:
        pg.display.update()
        sleep(self.frametime)
        self.screen.fill((0,0,0))

    def inputs(self) -> list:
        key = pg.key.get_pressed()
        pressed = []
        print(type(key))
        for k in key.keys():
            if key[k]==True:
                print(k)
                pressed.append(k)
        return pressed

    def close(self) -> None:
        pg.quit()

if __name__ == "__main__":
    r = rendering()
    while r.end_condition():
            r.loop()
            r.render_item([100,100],10)






