import numpy as np
import matplotlib.pyplot as plt

GRAVITY: float = 0.
BOUNDS: list = [800.,600.]
RESIST: float = 0.99
ELASTICITY: float = 0.8

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
        if self.x < 5:
            self.vx = ELASTICITY*abs(self.vx)
        elif self.x > BOUNDS[0]-5:
            self.vx = -ELASTICITY*abs(self.vx)
        if self.y < 5:
            self.vy = ELASTICITY*abs(self.vy)
        elif self.y > BOUNDS[1]-5:
            self.vy = -ELASTICITY*abs(self.vy)
        
        self.x += self.vx
        self.y += self.vy
        self.vy += GRAVITY

        self.vx *= RESIST
        self.vy *= RESIST
    
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
        return np.sqrt(dx**2 + dy**2)
    
    def collide(self) -> None:
        dx = self.o1.get_pos()[0] - self.o2.get_pos()[0]
        dy = self.o1.get_pos()[1] - self.o2.get_pos()[1]
        d = self.dist()
        ratio = self.o1.m/self.o2.m
        self.o1.push([ratio*dx/d, ratio*dy/d])
        ratio = -1/ratio
        self.o2.push([ratio*dx/d, ratio*dy/d])

class scene:
    def __init__(self) -> None:
        self.objects: list = []
        self.history: dict = {}

    def track(self, obj: object) -> None:
        self.objects.append(obj)
        self.history[obj] = [obj.get_pos()]
    
    def locate(self) -> None:
        print("\nLocations:")
        for obj in self.history:
            print(self.history[obj][len(self.history[obj])-5:])
    
    def traces(self, n:int=100) -> None:
        xs = []
        ys = []
        for obj in self.history:
            x = []
            y = []
            for xy in self.history[obj]:
                x.append(xy[0])
                y.append(xy[1])
            xs.append(x)
            ys.append(y)

        
        for i in range(len(xs)):
            m = (len(xs[i]) - n)//len(xs[i])
            plt.scatter(xs[i][m:],ys[i][m:])
        plt.show()

    def update(self,n: int = 1) -> None:
        for _ in range(n):
            for ob1 in self.objects:
                for ob2 in self.objects:
                    if ob1 != ob2:
                        interact(ob1, ob2)
            for ob in self.objects:
                ob.update()
                self.history[ob].append(ob.get_pos())




def main() -> None:
    blob =          object(pos=[50.,100.])
    blob.push([6.3,10.])
    other_blob =    object(pos=[100.,100.])
    other_blob.push([0.,10.])

    s = scene()
    s.track(blob)
    s.track(other_blob)

    MAXTIME = 200
    s.update(MAXTIME)

    s.traces()

if __name__ == "__main__":
    main()


