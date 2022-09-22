import turtle;

t = turtle.Turtle()


def create_stair(size: int, nb_step: int):
    t.forward(size)
    for _ in range(nb_step):
        t.left(90)
        t.forward(size)
        t.right(90)
        t.forward(size)
        size -= 3


def create_square(size: int):
    for _ in range(4):
        t.left(90)
        t.forward(size)


def create_square_bis(size: int):
    for _ in range(4):
        t.forward(size)
        t.left(90)


def create_many_squares(size: int, nb_square: int):
    for _ in range(nb_square):
        create_square(size)
        size += 25


create_many_squares(50, 7)

# t.circle(50, 360)

turtle.done()
