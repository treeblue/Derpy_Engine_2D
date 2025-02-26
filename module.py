#import numpy as np

GRAVITY = -9.8

class object:
    def __init__(self, pos:list[float]=[0.,0.], vel:list[float]=[0.,0.], mass:float=1) -> None:
        self.m: float = mass
        self.x: float = pos[0]
        self.y: float = pos[1]
        self.vx: float = vel[0]
        self.vy: float = vel[1]

    def get_pos(self) -> tuple[float]:
        return (self.x,self.y)
    
    def update_pos(self) -> None:
        self.x += self.vx
        self.y += self.vy
        self.vy += GRAVITY

    def cont_update(self, n:int) -> None:
        for _ in range(n):
            self.update_pos()
    
    def push(self, bump:list[float]) -> None:
        self.vx += bump[0]
        self.vy += bump[1]


def main() -> None:
    blob = object()
    print(blob.get_pos())
    blob.push([10,10])
    blob.update_pos()
    print(blob.get_pos())

if __name__ == "__main__":
    main()

