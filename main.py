# Case-study #1
# Developers: Khramchikhina A., Peshkov Y., Sanzhanova A., Yurshenaite A.
#

import turtle
turtle.pendown()
turtle.left(90)


def square(x, y, length, line_color, filling_color):
    '''
    Function, drawing a square.
    :param x: lower left corner coordinate x
    :param y: lower left corner coordinate y
    :param length: side length of a square
    :param line_color: color of square outline
    :param filling_color: inner color of square
    :return: None
    '''
    turtle.up()
    turtle.setposition(x, y)
    turtle.down()
    turtle.color(line_color, filling_color)
    turtle.begin_fill()
    turtle.forward(length)
    turtle.right(90)
    turtle.forward(length)
    turtle.right(90)
    turtle.forward(length)
    turtle.right(90)
    turtle.forward(length)
    turtle.right(90)
    turtle.end_fill()


def leg_triangle(x, y, leg_length, line_color, filling_color):
    '''
    Function, drawing an isosceles right triangle using the length of the leg.
    :param x: lower acute angle of triangle providing the triangle faces to the right coordinate x
    :param y: lower acute angle of triangle providing the triangle faces to the right coordinate y
    :param leg_length: length of the triangle leg
    :param line_color: color of triangle outline
    :param filling_color: inner color of triangle
    :return: None
    '''
    turtle.up()
    turtle.setposition(x, y)
    turtle.down()
    turtle.color(line_color, filling_color)
    turtle.begin_fill()
    turtle.forward((2*leg_length**2)**0.5)
    turtle.right(135)
    turtle.forward(leg_length)
    turtle.right(90)
    turtle.forward(leg_length)
    turtle.right(135)
    turtle.end_fill()


def hypotenuse_triangle(x, y, hypotenuse_length, line_color, filling_color):
    '''
    Function, drawing an isosceles right triangle using the length of the hypotenuse.
    :param x: lower acute angle of triangle providing the triangle faces to the right coordinate x
    :param y: lower acute angle of triangle providing the triangle faces to the right coordinate y
    :param hypotenuse_length: length of the triangle hypotenuse
    :param line_color: color of triangle outline
    :param filling_color: inner color of triangle
    :return: None
    '''
    turtle.up()
    turtle.setposition(x, y)
    turtle.down()
    turtle.color(line_color, filling_color)
    turtle.begin_fill()
    turtle.forward(hypotenuse_length)
    turtle.right(135)
    turtle.forward((0.5*hypotenuse_length**2)**0.5)
    turtle.right(90)
    turtle.forward((0.5*hypotenuse_length**2)**0.5)
    turtle.right(135)
    turtle.end_fill()


def parallelogram(x, y, length, height,  line_color, filling_color):
    '''
    Function, drawing parallelogram.
    :param x: lower left acute angle of parallelogram coordinate x
    :param y: lower left acute angle of parallelogram coordinate y
    :param length: side length of the parallelogram
    :param height: height of parallelogram
    :param line_color: color of parallelogram outline
    :param filling_color: inner color of parallelogram
    :return: None
    '''
    turtle.up()
    turtle.setposition(x, y)
    turtle.down()
    turtle.color(line_color, filling_color)
    turtle.begin_fill()
    turtle.right(45)
    turtle.forward(height/((2**0.5)/2))
    turtle.right(45)
    turtle.forward(length)
    turtle.right(135)
    turtle.forward(height / ((2 ** 0.5) / 2))
    turtle.right(45)
    turtle.forward(length)
    turtle.right(45)
    turtle.end_fill()


def rectangle(x, y, length, height, line_color, filling_color):
    '''
    Function, drawing a rectangle.
    :param x: lower left corner coordinate x
    :param y: lower left corner coordinate y
    :param length: side length of the rectangle
    :param height: height of the rectangle
    :param line_color: color of rectangle outline
    :param filling_color: inner color of rectangle
    :return: None
    '''
    turtle.up()
    turtle.setposition(x, y)
    turtle.down()
    turtle.color(line_color, filling_color)
    turtle.begin_fill()
    turtle.forward(height)
    turtle.right(90)
    turtle.forward(length)
    turtle.right(90)
    turtle.forward(height)
    turtle.right(90)
    turtle.forward(length)
    turtle.right(90)
    turtle.end_fill()
    

def main_square(x, y, length):
    '''
    Function, drawing square in the middle made of figures.
    :param x: right(90) angle of the blue triangle in the middle coordinate x
    :param y: right angle(90) of the blue triangle in the middle coordinate y
    :param length: side length of a main square
    :return: None
    '''
    hypotenuse_triangle(x-0.5*length, y-0.5*length, length, 'white', 'red')
    turtle.right(90)
    hypotenuse_triangle(x-0.5*length, y+0.5*length, length, 'white', 'orange')
    turtle.right(90)
    hypotenuse_triangle(x+0.5*length, y+0.5*length, 0.5*length, 'white', 'yellow')
    turtle.right(225)
    leg_triangle(x, y-0.5*length, 0.5*length, 'white', 'green')
    square(x, y, (0.5*(0.5*length)**2)**0.5, 'white', 'cyan')
    turtle.left(135)
    hypotenuse_triangle(x+0.25*length, y-0.25*length, 0.5*length, 'white', 'blue')
    turtle.right(90)
    parallelogram(x-0.5*length, y-0.5*length, 0.5*length, 0.25*length, 'white', 'purple')
    turtle.right(45)


def rabbit(x, y, length):
    '''
    Function, drawing a rabbit.
    :param x: lower left corner of square coordinate x
    :param y: lower left corner of square coordinate y
    :param length: length of a rabbit from back(left angle of cyan triangle) to head(lower right corner of square)
    :return: None
    '''
    square(x, y, 1/3*length, 'white', 'red')
    turtle.right(45)
    leg_triangle(x-2/3*length, y-0.5*length, 2/3*length, 'white', 'orange')
    turtle.right(180)
    leg_triangle(x, y-0.5*length, 2/3*length, 'white', 'yellow')
    turtle.right(135)
    hypotenuse_triangle(x, y-2/3*length, 1/3*length, 'white', 'green')
    turtle.right(45)
    leg_triangle(x-2/3*length, y-7/6*length, 0.5*length, 'white', 'cyan')
    turtle.right(90)
    leg_triangle(x-1/6*length, y-5/6*length, 1/3*length, 'white', 'blue')
    turtle.right(90)
    parallelogram(x+1/6*length, y+1/3*length, 0.5*length, 1/6*length, 'white', 'purple')
    turtle.right(180)


def fish(x, y, height):
    '''
    Function, drawing a fish.
    :param x: lower corner of red triangle coordinate x
    :param y: lower corner of red triangle coordinate y
    :param height: distance between two right(90) angles of red and orange triangles
    :return: None
    '''
    turtle.left(45)
    leg_triangle(x, y, 0.5*height, 'white', 'red')
    turtle.right(90)
    leg_triangle(x-0.5*height, y-0.5*height, 0.5*height, 'white', 'orange')
    turtle.left(45)
    hypotenuse_triangle(x, y-0.25*height, 0.5*height, 'white', 'yellow')
    turtle.left(135)
    square(x, y, 0.25*height, 'white', 'green')
    parallelogram(x-(2*((0.25*height)**2))**0.5, y, 0.375*height, 0.1925*height, 'white', 'cyan')
    turtle.right(45)
    hypotenuse_triangle(x-(2*(0.25*height)**2)**0.5, y, 0.375*height,  'white', 'blue')
    turtle.right(180)
    hypotenuse_triangle(x-(2*(0.25*height)**2)**0.5-2*((0.5*((0.375*height)**2))**0.5), y-((0.5*((0.375*height)**2))**0.5), 0.375*height, 'white', 'purple')
    turtle.left(45)


def rooster(x, y, length):
    '''
    Function, drawing a rooster.
    :param x: lower left corner of square coordinate x
    :param y: lower left corner of square coordinate y
    :param length: length of the rooster from left angle of pink triangle to right corner of square
    :return: None
    '''
    square(x, y, 1/4*length, 'white', 'orange')
    turtle.left(90)
    hypotenuse_triangle(x + 1/4*1.5*length, y+1/4*length, 1/4*1.5*length, 'white', 'blue')
    turtle.left(45)
    leg_triangle(x + 1/4 * length, y, 1/2*length, 'white', 'yellow')
    turtle.left(45)
    hypotenuse_triangle(x + 1/8*length, y - (1/2-(1.5*1/4))*length, 1.5*1/4*length, 'white', 'BlueViolet')
    turtle.right(135)
    leg_triangle(x - 1/4*length, y - 1/4*length, 1/2*length, 'white', 'magenta')
    turtle.left(45)
    hypotenuse_triangle(x - 1/4*length, y + 1/4*length, 1/2*length, 'white', 'cyan')
    turtle.left(180)
    parallelogram(x - 3/4*length, y + 1/4*length, 1/3*length, 1/8*length, 'white', 'LimeGreen')
    turtle.left(45)


def ship(x, y, length):
    '''
    Function, drawing a boat.
    :param x: lower angle of red triangle coordinate x
    :param y: lower angle of red triangle coordinate y
    :param length: distance between upper angle of black triangle and lower side of parallelogram
    :return: None
    '''
    hypotenuse_triangle(x, y, 20/33*length, 'white', 'red')
    turtle.right(135)
    leg_triangle(x, y+26/33*length, 2/11*length, 'white', 'black')
    turtle.left(90)
    leg_triangle(x-16/33*length, y+2/33*length, 16/33*length, 'white', 'yellow')
    turtle.left(135)
    hypotenuse_triangle(x+10/33*length, y, 10/33*length, 'white', 'green')
    turtle.right(45)
    square(x+10/33*length, y, (0.5*(10/33*length)**2)**0.5, 'white', 'cyan')
    turtle.right(135)
    hypotenuse_triangle(x-4/33*length, y, 14/33*length, 'white', 'blue')
    turtle.right(135)
    parallelogram(x+1/11*length, y-7/33*length, (0.5*(14/33*length)**2)**0.5, 5/33*length, 'white', 'purple')
    turtle.right(180)


def helicopter(x, y, length):
    '''
    Function, drawing a helicopter.
    :param x: right(90) angle of purple triangle coordinate x
    :param y: middle of hypotenuse of red triangle coordinate y
    :param length: distance between upper angle of blue triangle and lower angle of red triangle
    :return: None
    '''
    parallelogram(x+1/5*length, y + 1/4*length, 1/2.5*length, 1/6*length, 'white', 'LimeGreen')
    turtle.right(45)
    hypotenuse_triangle(x + 1/5*length, y - 1/2*length, 3/4*length, 'white', 'red')
    turtle.right(180)
    hypotenuse_triangle(x+1/5*length, y+1/4*length, 3/4*length, 'white', 'yellow')
    turtle.right(90)
    hypotenuse_triangle(x+1/5*length, y+1/4*length, 1/2*length, 'white', 'blue')
    leg_triangle(x, y-1/3.25*length, 1/4*length, 'white', 'purple')
    turtle.right(180)
    leg_triangle(x-1/1.875*length, y-1/8.5*length, 1/4*length, 'white', 'pink')
    turtle.left(135)
    square(x-1/1.5*length, y-1/4*length, 1/4*length, 'white', 'orange')
    turtle.right(45)
    

def f1_car(x, y, length):
    '''
    Function, drawing a formula-1 car.
    :param x: right angle of black triangle(rear wing) coordinate x
    :param y: right angle of black triangle(rear wing) coordinate y
    :param length: length from left corner of black triangle(rear wing) and right angle of red square(front wing)
    :return: None
    '''
    turtle.right(45)
    leg_triangle(x, y, 0.24*length, 'red', 'black')
    turtle.left(45)
    square(x+0.24*length, y-0.16*length, 0.16*length, 'black', 'black')
    turtle.right(45)
    leg_triangle(x+0.24*length, y, 0.16*length, 'red', 'red')
    turtle.left(45)
    rectangle(x+0.4*length, y-0.08*length, 0.32*length, 0.08*length, 'red', 'red')
    square(x+0.72*length, y-0.16*length, 0.16*length, 'black', 'black')
    turtle.right(135)
    leg_triangle(x+0.88*length, y+0.04*length, 0.12*length, 'black', 'red')
    leg_triangle(x+0.4*length, y+0.16*length, 0.16*length, 'red', 'red')
    turtle.right(180)
    leg_triangle(x+0.56*length, y, 0.16*length, 'red', 'black')
    turtle.right(45)
    rectangle(x+0.56*length, y, 0.32*length, 0.04*length, 'red', 'red')


def left_man(x, y, length):
    '''
    Function, drawing a man running on the left side.
    :param x: right angle of red triangle coordinate x
    :param y: right angle of red triangle coordinate y
    :param length: length from right angle of red triangle to left angle of the orange triangle
    :return: None
    '''
    turtle.right(45)
    leg_triangle(x, y, 2/3*length, 'white', 'red')
    turtle.right(180)
    leg_triangle(x+length, y+length, 2/3*length, 'white', 'orange')
    turtle.right(90)
    square(x+0.5*length, y+length, 1/3*length, 'white', 'brown')
    parallelogram(x, y+1/3*length, (2*(1/3*length)**2)**0.5, 7/30*length, 'white', 'green')
    turtle.left(45)
    leg_triangle(x+2/15*length, y+2/15*length, 1/3*length, 'white', 'cyan')
    turtle.right(135)
    hypotenuse_triangle(x+2/3*length, y-0.4*length, 8/15*length, 'white', 'blue')
    turtle.right(180)
    hypotenuse_triangle(x+2/3*length, y-0.2*length, 1/3*length, 'white', 'purple')
    turtle.right(180)


def right_man(x, y, length):
    '''
    Function, drawing a man running on the right side.
    :param x: lower angle of orange triangle coordinate x
    :param y: lower angle of orange triangle coordinate y
    :param length: length from right(90) angle of orange triangle to right(90) angle of the red triangle
    :return: None
    '''
    turtle.left(45)
    leg_triangle(x, y, 2/3*length, 'white', 'orange')
    turtle.left(90)
    leg_triangle(x+2/3*length, y+2/3*length, 2/3*length, 'white', 'green')
    turtle.right(90)
    square(x, y+2/3*length, 1/3*length, 'white', 'brown')
    turtle.right(180)
    leg_triangle(x, y, 1/3*length, 'white', 'red')
    turtle.right(180)
    leg_triangle(x+7/15*length, y-0.6*length, 4/15*length, 'white', 'cyan')
    turtle.left(180)
    parallelogram(x, y, 0.4*length, 0.2*length, 'white', 'blue')
    turtle.left(45)
    leg_triangle(x-1/3*length, y-19/30*length, 0.2*length, 'white', 'purple')
    turtle.left(45)


def main():
    '''
    Main function.
    :return: None
    '''
    rabbit(-200, 240, 95)
    fish(50, 215, 150)
    rooster(235, 200, 150)
    ship(-225, -210, 150)
    helicopter(0, -175, 150)
    f1_car(120, -200, 195)
    left_man(-260, -25, 88)
    right_man(235, -15, 100)
    main_square(0, 15, 200)
    turtle.done()


if __name__ == '__main__':
    main()
 