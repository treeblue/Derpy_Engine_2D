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

    def render_item(self, location:list, size:float, colour:tuple=(0,0,200)) -> None:
        R = pg.Rect((location[0],location[1],size,size))
        pg.draw.rect(self.screen,colour,R)

    def loop(self):
        pg.display.update()
        sleep(self.frametime)
        self.screen.fill((0,0,0))

    def __exit__(self):
        pg.quit()

if __name__ == "__main__":
    r = rendering()
    while r.end_condition():
            r.loop()
            r.render_item([100,100],10)






