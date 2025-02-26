# import numpy as np

GRAVITY = 0.

class object:
    def __init__(self, pos:list=[0.,0.], vel:list=[0.,0.], mass:float=1) -> None:
        self.m: float = mass
        self.x: float = pos[0]
        self.y: float = pos[1]
        self.vx: float = vel[0]
        self.vy: float = vel[1]

    def get_pos(self) -> tuple:
        return (self.x,self.y)
    
    def update(self) -> None:
        self.x += self.vx
        self.y += self.vy
        self.vy += GRAVITY

    def cont_update(self, n:int) -> None:
        for _ in range(n):
            self.update_pos()
    
    def push(self, bump:list) -> None:
        self.vx += bump[0]
        self.vy += bump[1]

class interact:
    def __init__(self, o1:object, o2:object) -> None:
        self.o1 = o1
        self.o2 = o2
        self.range = 10.
        if self.dist() < self.range:
            self.collide()
    
    def dist(self) -> float:
        dx = self.o1.get_pos()[0] - self.o2.get_pos()[0]
        dy = self.o1.get_pos()[1] - self.o2.get_pos()[1]
        return dx**2 + dy**2
    
    def collide(self) -> None:
        dx = self.o1.get_pos()[0] - self.o2.get_pos()[0]
        dy = self.o1.get_pos()[1] - self.o2.get_pos()[1]
        ratio = self.o1.m/self.o2.m
        self.o1.push([ratio*dx, ratio*dy])
        ratio = -1/ratio
        self.o2.push([ratio*dx, ratio*dy])

def main() -> None:
    blob = object()
    other_blob = object()
    blob.push([1,0])
    blob.update()

    print(blob.get_pos(),other_blob.get_pos())
    interact(blob,other_blob)
    blob.update()
    other_blob.update()
    print(blob.get_pos(),other_blob.get_pos())
    blob.update()
    other_blob.update()
    print(blob.get_pos(),other_blob.get_pos())

if __name__ == "__main__":
    main()

