import math
import turtle as t


def triangle(x: int, y: int, a: int, b: int, col: str) -> None:
    """
    Draws an isosceles triangle.

    :param int x: X coordinate of the left end of the base
    :param int y: Y coordinate of the left end of the base
    :param int a: Length of the equal sides (legs)
    :param int b: Length of the base
    :param str col: Fill color of the triangle
    :return: None
    """
    t.fillcolor(col)
    t.begin_fill()
    t.up()
    t.goto(x, y)
    t.down()
    t1 = math.degrees(math.acos(b / (2 * a)))
    t2 = math.degrees(math.acos(1 - (b**2 / (2 * a**2))))
    t.forward(b)
    t.left(180 - t1)
    t.forward(a)
    t.left(180 - t2)
    t.forward(a)
    t.end_fill()
    t.up()
    t.home()


def right_triangle_2(x: int, y: int, a: int, b: int, col: str) -> None:
    """
    Draws a rectangular triangle (mirrored).

    :param int x: x coordinates of start point
    :param int y: coordinates y starting point
    :param int a: first skate
    :param int b: second skate
    :param str col: Color of the curd and contour
    :return: None
    """
    t.up()
    t.setposition(x, y)
    t.down()
    t.fillcolor(col)
    t.begin_fill()
    t.forward(a)
    t.right(90)
    t.forward(b)
    c = math.sqrt(a ** 2 + b ** 2)
    o = math.degrees(math.atan(a / b))
    t.right(180 - o)
    t.forward(c)
    t.end_fill()
    t.up()
    t.home()


def ornament_square() -> None:
    """
    Draws a symmetric ornamental pattern of triangles from four squares.

    The pattern consists of blue right triangles and white/crimson isosceles
    triangles arranged around the center. The turtle is repositioned and
    rotated to draw each quadrant sequentially.

    :return: None
    """
    # First square.
    right_triangle_2(-300, 300, 300, 300, "royal blue")
    t.right(90)
    triangle(-300, 300, 212, 300, "white")
    triangle(-300, 0, 212, 300, "crimson")
    # Second square.
    t.left(90)
    right_triangle_2(-300, -300, 300, 300, "royal blue")
    triangle(-300, -300, 212, 300, "white")
    t.left(90)
    triangle(0, -300, 212, 300, "crimson")
    # Third square
    t.left(180)
    right_triangle_2(300, -300, 300, 300, "royal blue")
    t.left(90)
    triangle(300, -300, 212, 300, "white")
    t.left(180)
    triangle(300, 0, 212, 300, "crimson")
    #Fouf square
    t.right(90)
    right_triangle_2(300, 300, 300, 300, "royal blue")
    t.left(180)
    triangle(300, 300, 212, 300, "white")
    t.right(90)
    triangle(0, 300, 212, 300, "crimson")


if __name__ == "__main__":
    t.speed(10)
    t.pensize(2)
    t.screensize(800, 800)
    t.pencolor('black')
    ornament_square()
    t.hideturtle()
    t.done()
