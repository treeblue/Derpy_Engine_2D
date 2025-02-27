from src.physics import object, scene
from src.game import rendering
import pygame as pg

#This uses classes from physics.py and game.py

size = [800,600]
r = rendering(size)

p1 = object(pos=[size[0]/2,size[1]/2],vel=[10.,0])
other = object(pos=[size[0]/3,size[1]/2])

frame = scene()
frame.track(p1)
frame.track(other)

if __name__ == "__main__":
    i = 0
    while r.end_condition():
        r.loop()
        # i += 1
        # print(f"Frame: {i}")
        frame.update()
        for obj in frame.objects:
            xy = obj.get_pos()
            r.render_item(xy,10)
        pressed = r.inputs()
        # print(pressed)
    r.close()
    # frame.traces()
