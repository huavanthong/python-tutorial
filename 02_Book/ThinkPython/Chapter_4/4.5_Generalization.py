from swampy.TurtleWorld import * 

def square(t, length):
    for i in range(4):
        fd(t, length)
        lt(t)


def polygon(t, n, length):
    angle = 360.0 / n
    for i in range(n):
        fd(t, length)
        lt(t, angle)

def main():
    # Create windows
    world = TurtleWorld()

    # Tạo đối tượng turtle
    bob = Turtle()

    # Vẽ một hình vuông với độ dài cạnh là 100.
    square(bob, 100)

    # Vẽ một đa giác 7 cạnh với độ dài cạnh là 70
    # Đây cũn
    polygon(bob, n=7, length=70)

    # Đợi user 
    wait_for_user()

if __name__ == '__main__':
    main()