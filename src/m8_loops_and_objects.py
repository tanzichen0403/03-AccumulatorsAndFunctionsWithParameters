"""
This module demonstrates simple LOOPS of the form:
   for k in range(blah):
      ... k ...

and also USING OBJECTS.

Authors: David Mutchler, Vibha Alangar, Matt Boutell, Dave Fisher, Mark Hays,
         Aaron Wilkin, their colleagues, and Zichen Tan.
"""  # Done: 1. PUT YOUR NAME IN THE ABOVE LINE.

import rosegraphics as rg
import math


def main():
    """ Calls the other functions to demonstrate and/or test them. """
    # Test your functions by putting calls to them here:
    print_sequence1(20)
    draw_circles1(20)
    print_sequence2(20)
    draw_circles2(10)
    print_sequence3(20)
    draw_circles3(5)
    print_cosines(5)
    draw_cosines_and_sines(5)
def print_sequence1(n):
    """
    Prints:
       0
       10
       20
       30
       40
       ...
       200
    """
    # -------------------------------------------------------------------------
    # Done: 2. Implement this function, per its doc-string above.
    # Put a statement in  main  to test this function.
    # REQUIREMENT: You must use a   RANGE  statement to solve this problem.
    # -------------------------------------------------------------------------
    print()
    print('--------------------------------------------------')
    print('Running print_sequence1:')
    print('--------------------------------------------------')
    t=0
    for k in range(n+1):

        print(t*10)
        t=t+1


def draw_circles1(n):
    """
    -- Constructs an rg.RoseWindow whose width and height are both 400.
    -- Constructs and draws 21 rg.Circle objects such that:
         -- Each is centered at (200, 200)
         -- They have radii:  0  10  20  30  40 ... 200, respectively.
    -- Waits for the user to press the mouse, then closes the window.
    """
    # -------------------------------------------------------------------------
    # Done: 3. Implement this function, per its doc-string above.
    # Put a statement in  main  to test this function.
    # REQUIREMENT: You must use a   RANGE  statement to solve this problem.
    # HINT: You might find a prior module useful when 'writing' this code.
    # -------------------------------------------------------------------------
    print()
    print('--------------------------------------------------')
    print('Running draw_circles1:  See graphics window')
    print('--------------------------------------------------')
    betterdraw(n)
    window = rg.TurtleWindow()
    window.update()
    window.close_on_mouse_click()

def betterdraw (x) :
    turtle = rg.SimpleTurtle()
    turtle.pen_up()
    point = rg.Point(200, 200)
    turtle.go_to(point)
    turtle.pen_down()
    turtle.set_heading(0)
    t=0
    turtle.speed=20
    for k in range(x+1):
        t = t + 1
        turtle.pen_up()
        turtle.right(90 )
        turtle.forward(10 )
        turtle.left(90 )
        turtle.pen_down()
        turtle.draw_circle(10 * t)



def print_sequence2(n):
    """
    Prints:
      50
      70
      90
      110
      130
      ...
      390.
    """
    # -------------------------------------------------------------------------
    # DOne: 4. Implement this function, per its doc-string above.
    # Put a statement in  main  to test this function.
    # REQUIREMENT: You must use a   RANGE  statement to solve this problem.
    # -------------------------------------------------------------------------
    print()
    print('--------------------------------------------------')
    print('Running print_sequence2:')
    print('--------------------------------------------------')
    for k in range(n):
        t=50+k*20
        print(t)

def draw_circles2(n):
    """
    -- Constructs an rg.RoseWindow whose width and height are both 400.
    -- Constructs and draws rg.Circle objects such that:
         -- Each has radius 10.
         -- Each has fill_color 'blue'.
         -- They are centered at, respectively:
               (50, 100)   (70, 100)   (90, 100)  (110, 100) ... (390, 100)
    -- Waits for the user to press the mouse, then closes the window.
    """
    # -------------------------------------------------------------------------
    # DOne: 5. Implement this function, per its doc-string above.
    # Put a statement in  main  to test this function.
    # REQUIREMENT: You must use a   RANGE  statement to solve this problem.
    # -------------------------------------------------------------------------
    print()
    print('--------------------------------------------------')
    print('Running draw_circles2:  See graphics window')
    print('--------------------------------------------------')
    betterdraw1(n)
    window = rg.TurtleWindow()
    window.update()
    window.close_on_mouse_click()
def betterdraw1 (x) :
    for k in range(x):
        turtle = rg.SimpleTurtle()
        turtle.pen_up()
        point=rg.Point(50+k*20,100)
        turtle.go_to(point)
        turtle.pen_down()
        turtle.set_heading(0)
        turtle.pen_up()
        turtle.right(90 )
        turtle.forward(10 )
        turtle.left(90 )
        turtle.pen_down()
        turtle.draw_circle(10)

def print_sequence3(n):
    """
    Prints:
      1
      2
      3 
      4
      ...
      100.
    """
    # -------------------------------------------------------------------------
    # Done: 6. Implement this function, per its doc-string above.
    # Put a statement in  main  to test this function.
    # REQUIREMENT: You must use a   RANGE  statement to solve this problem.
    # -------------------------------------------------------------------------
    print()
    print('--------------------------------------------------')
    print('Running print_sequence3:')
    print('--------------------------------------------------')
    t=0
    for k in range (n):
        t=t+1
        print(t)


def draw_circles3(n):
    """
    -- Constructs an rg.RoseWindow whose width and height are both 300.
    -- Constructs and draws 100 rg.Circle objects such that:
         -- Each is centered at (200, 150)
         -- They have radii:  1  2  3  4  ... 100, respectively.
    -- Waits for the user to press the mouse, then closes the window.
    """
    # -------------------------------------------------------------------------
    # Done: 7. Implement this function, per its doc-string above.
    # Put a statement in  main  to test this function.
    # REQUIREMENT: You must use a   RANGE  statement to solve this problem.
    # -------------------------------------------------------------------------
    print()
    print('--------------------------------------------------')
    print('Running draw_circles3:  See graphics window')
    print('--------------------------------------------------')
    betterdraw2(n)
    window = rg.TurtleWindow()
    window.update()
    window.close_on_mouse_click()
def betterdraw2 (x):
    turtle = rg.SimpleTurtle()
    turtle.pen_up()
    point = rg.Point(200, 150)
    turtle.go_to(point)
    turtle.pen_down()
    turtle.set_heading(0)
    turtle.speed=10
    for k in range(x):
        turtle.pen_up()
        turtle.right(90)
        turtle.forward(1)
        turtle.left(90)
        turtle.pen_down()
        turtle.draw_circle(k+1)

def print_cosines(n):
    """
    For each of the integers 0  1  2  ... 100,
    prints 80 times the cosine of that integer.
    Thus, the numbers printed should be about:
       80.0
       43.224184469451174
       -33.29174692377139
       -79.19939972803563
       -52.29148966908895
       22.6929748370581
       76.81362293202928
       60.31218034746437
         ...
       -65.54305962331674
       3.185670431451112
       68.9855097830147
    """
    # -------------------------------------------------------------------------
    # Done: 8. Implement this function, per its doc-string above.
    # Put a statement in  main  to test this function.
    # REQUIREMENT: You must use a   RANGE  statement to solve this problem.
    #
    # HINT: You need to   import math   at the top of this file
    #       to use math functions like the ones for cosine and sine.
    #       Once you have that import in place, typing
    #            math.
    #       (note the DOT) and pausing will display options that make
    #       it plain what the notation for the cosine function is.
    # -------------------------------------------------------------------------
    print()
    print('--------------------------------------------------')
    print('Running print_cosines:')
    print('--------------------------------------------------')
    for k in range(n):
        t=80*math.cos(k)
        print(t)

def draw_cosines_and_sines(n):
    """
    -- Constructs a window whose width and height are both 400.
    -- Constructs and draws rg.Circle objects such that:
         -- Each has radius 10.
         -- They are centered at, respectively:
               ( 200 + (80 * cos(0)), 200 + (80 * sin(0) )
               ( 200 + (80 * cos(1)), 200 + (80 * sin(1) )
               ( 200 + (80 * cos(2)), 200 + (80 * sin(2) )
               ( 200 + (80 * cos(3)), 200 + (80 * sin(3) )
                   ...
               ( 200 + (80 * cos(100)), 200 + (80 * sin(100) )
    -- Waits for the user to press the mouse, then closes the window.
    """
    # -------------------------------------------------------------------------
    # Done: 9. Implement this function, per its doc-string above.
    # Put a statement in  main  to test this function.
    # REQUIREMENT: You must use a   RANGE  statement to solve this problem.
    # -------------------------------------------------------------------------
    print()
    print('--------------------------------------------------')
    print('Running draw_cosines_and_sines:  See graphics window')
    print('--------------------------------------------------')
    window = rg.TurtleWindow()
    window.update()
    turtle = rg.SimpleTurtle()
    turtle.pen_up()
    turtle.speed=10
    for k in range(n):
        t=200+80*math.cos(k)
        m=200+80*math.sin(k)
        turtle.pen_up()
        point = rg.Point(t, m)
        turtle.go_to(point)
        turtle.pen_down()
        turtle.set_heading(0)
        turtle.pen_up()
        turtle.right(90)
        turtle.forward(10)
        turtle.left(90)
        turtle.pen_down()
        turtle.draw_circle(10)
    window.close_on_mouse_click()




# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()
