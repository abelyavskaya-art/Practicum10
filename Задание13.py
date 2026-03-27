import turtle as t


def triangle(x1: int, y1: int, x2: int,
             y2: int, x3: int, y3: int, col: str) -> None:
    """
    Constructs a triangle based on the coordinates
    of three vertices and a given color.

    :param float x1: Coordinate x first vertex
    :param float y1: Coordinates y first vertex
    :param float x2: Coordinate x second vertex
    :param float y2: Coordinates y second vertex
    :param float x3: Coordinate x third vertex
    :param float y3: Coordinates y third vertex
    :param str col: Color of triangle inlet
    :return: None
    """
    t.fillcolor(col)
    t.begin_fill()

    t.penup()
    t.goto(x1, y1)
    t.pendown()
    t.goto(x2, y2)
    t.goto(x3, y3)
    t.goto(x1, y1)

    t.end_fill()

def square1(x: int, y: int, side: int,
            col1: str, col2: str) -> None:
    """
    Type 1 square: diagonal from right bottom to left top corner.

    :param float x: Coordinate x of the lower left corner of a square
    :param float y: The y coordinates of the lower left corner of a square
    :param float side: Square side length
    :param str col1: First triangle color (lower right)
    :param str col2: Color of the second triangle (upper left)
    :return: None
    """
    # The vertices of the quadrate.
    left_bottom = (x, y)
    right_bottom = (x + side, y)
    left_top = (x, y + side)
    right_top = (x + side, y + side)

    # First triangle (lower right).
    triangle(
        left_bottom[0], left_bottom[1],
        right_bottom[0], right_bottom[1],
        right_top[0], right_top[1],
        col1
    )

    # Second triangle (upper left).
    triangle(
        left_top[0], left_top[1],
        left_bottom[0], left_bottom[1],
        right_top[0], right_top[1],
        col2
    )


def square2(x: int, y: int, side: int,
            col1: str, col2: str) -> None:
    """
    Type 2 quadrant: diagonal from lower left to upper right corner.
    First triangle (col1) - lower left,
    Second triangle (col2) - upper right.

    :param float x: Coordinate x of the lower left corner of a square
    :param float y: The y coordinates of the lower left corner of a square
    :param float side: Square side length
    :param str col1: First triangle color (lower left)
    :param str col2: Color of the second triangle (upper right)
    :return: None
    """
    # The vertices of the quadrate.
    left_bottom = (x, y)
    right_bottom = (x + side, y)
    left_top = (x, y + side)
    right_top = (x + side, y + side)

    # First triangle (lower left).
    triangle(
        left_bottom[0], left_bottom[1],
        right_bottom[0], right_bottom[1],
        left_top[0], left_top[1],
        col1
    )

    # Second triangle (upper right).
    triangle(
        right_top[0], right_top[1],
        left_top[0], left_top[1],
        right_bottom[0], right_bottom[1],
        col2
    )


def tile_pattern() -> None:
    """
    Constructs a pattern of 36 square.
    """
    start_x = -300
    start_y = -300
    tile_size = 100
    tiles_per_group = 3
    group_size = tile_size * tiles_per_group

    # Left bottom angle.
    for row in range(tiles_per_group):
        for col in range(tiles_per_group):
            x = start_x + col * tile_size
            y = start_y + row * tile_size
            square1(x, y, tile_size, "lightblue", "coral")

    # Right bottom angle.
    for row in range(tiles_per_group):
        for col in range(tiles_per_group):
            x = start_x + group_size + col * tile_size
            y = start_y + row * tile_size
            square2(x, y, tile_size, "coral", "lightblue")

    # Left top angle.
    for row in range(tiles_per_group):
        for col in range(tiles_per_group):
            x = start_x + col * tile_size
            y = start_y + group_size + row * tile_size
            square2(x, y, tile_size, "coral", "lightblue")

    # Right top angle.
    for row in range(tiles_per_group):
        for col in range(tiles_per_group):
            x = start_x + group_size + col * tile_size
            y = start_y + group_size + row * tile_size
            square1(x, y, tile_size, "lightblue", "coral")


if __name__ == "__main__":
    t.setup(800, 800)
    t.speed(10)
    t.hideturtle()

    tile_pattern()
    t.done()
