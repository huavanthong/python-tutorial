"""
    Write a function called square that takes a parameter named t, which is a turtle. It should use the turtle to draw a square.
    Write a function call that passes bob as an argument to square, and then run the program again.
"""
from swampy.TurtleWorld import * 

def square(t):
    for i in range(4):
        fd(t, 100)
        lt(t)


def main():
    world = TurtleWorld()
    bob = Turtle()

    square(bob)
    wait_for_user()


if __name__ == '__main__':
    main()