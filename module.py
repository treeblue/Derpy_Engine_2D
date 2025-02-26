#import numpy as np



class object:
    def __init__(self) -> None:
        self.x: float = 0
        self.y: float = 0
        self.vx: float = 0
        self.vy: float = 0

    def get_position(self) -> tuple:
        return (self.x,self.y)


def main() -> None:
    blob = object()
    print(blob.get_position())

if __name__ == "__main__":
    main()

