"""
This module lets you practice  ** using objects **, including:
  -- CONSTRUCTING objects,
  -- applying METHODS to them, and
  -- accessing their DATA via INSTANCE VARIABLES

Authors: David Mutchler, Vibha Alangar, Matt Boutell, Dave Fisher, Mark Hays,
         Aaron Wilkin, their colleagues, and Paige Swango.
"""  # DONE: 1. PUT YOUR NAME IN THE ABOVE LINE.

import rosegraphics as rg


def main():
    """ Calls the other functions to demonstrate and/or test them. """
    # Test your functions by putting calls to them here:
    two_circles()
    circle_and_rectangle()
    lines()

def two_circles():
    """
    -- Constructs an rg.RoseWindow.
    -- Constructs and draws two rg.Circle objects on the window
         such that:
           -- They fit in the window and are easily visible.
           -- They have different radii.
           -- One is filled with some color and one is not filled.
    -- Waits for the user to press the mouse, then closes the window.
    """
    # -------------------------------------------------------------------------
    # DONE: 2. Implement this function, per its green doc-string above.
    #    -- ANY two rg.Circle objects that meet the criteria are fine.
    #    -- File  COLORS.pdf  lists all legal color-names.
    # Put a statement in   main   to test this function
    #    (by calling this function).
    # -------------------------------------------------------------------------
    width = 400
    height = 400
    window = rg.RoseWindow(width, height)




    radius = 10
    radius2= 60
    center_point = rg.Point(100,200)
    circle = rg.Circle(center_point, radius)
    circle.fill_color = 'blue'
    circle.attach_to(window)
    circle2 = rg.Circle(center_point,radius2)
    circle2.attach_to(window)
    window.render()
    window.close_on_mouse_click()

def circle_and_rectangle():
    """
    -- Constructs an rg.RoseWindow.
    -- Constructs and draws a rg.Circle and rg.Rectangle
       on the window such that:
          -- They fit in the window and are easily visible.
          -- The rg.Circle is filled with 'blue'
    -- Prints (on the console, on SEPARATE lines) the following data
         associated with your rg.Circle:
          -- Its outline thickness.
          -- Its fill color.
          -- Its center.
          -- Its center's x coordinate.
          -- Its center's y coordinate.
    -- Prints (on the console, on SEPARATE lines) the same data
         but for your rg.Rectangle.
    -- Waits for the user to press the mouse, then closes the window.

    Here is an example of the output on the console,
    for one particular circle and rectangle:
           1
           blue
           Point(180.0, 115.0)
           180
           115
           1
           None
           Point(75.0, 150.0)
           75.0
           150.0
    """
    # -------------------------------------------------------------------------
    # DONE: 3. Implement this function, per its green doc-string above.
    #   -- ANY objects that meet the criteria are fine.
    # Put a statement in   main   to test this function
    #    (by calling this function).
    #
    # IMPORTANT: Use the DOT TRICK to guess the names of the relevant
    #       instance variables for outline thickness, etc.
    # -------------------------------------------------------------------------
    width= 400
    height= 400
    window = rg.RoseWindow(width,height)
    radius = 10
    center_point = rg.Point(100, 200)
    circle = rg.Circle(center_point, radius)
    circle.fill_color = 'blue'
    circle.attach_to(window)
    print(circle.outline_thickness)
    print(circle.fill_color)
    print(circle.center)
    print(circle.center.x)
    print(circle.center.y)

    corner_1= rg.Point(20,50)
    corner_2= rg.Point(70,150)
    rectangle= rg.Rectangle(corner_1,corner_2)
    rectangle.attach_to(window)
    print(rectangle.outline_thickness)
    print(rectangle.fill_color)
    print(rectangle.corner_1)
    print(rectangle.corner_2)


    window.render()
    window.close_on_mouse_click()



def lines():
    """
    -- Constructs a rg.RoseWindow.
    -- Constructs and draws on the window two rg.Lines such that:
          -- They both fit in the window and are easily visible.
          -- One rg.Line has the default thickness.
          -- The other rg.Line is thicker (i.e., has a bigger width).
    -- Uses a rg.Line method to get the midpoint (center) of the
         thicker rg.Line.
    -- Then prints (on the console, on SEPARATE lines):
         -- the midpoint itself
         -- the x-coordinate of the midpoint
         -- the y-coordinate of the midpoint

       Here is an example of the output on the console, if the two
       endpoints of the thicker line are at (100, 100) and (121, 200):
            Point(110.5, 150.0)
            110.5
            150.0

    -- Waits for the user to press the mouse, then closes the window.
    """
    # DONE: 4. Implement and test this function.
    width = 400
    height = 400
    window = rg.RoseWindow(width, height)
    point1=rg.Point(20,60)
    point2=rg.Point(50,100)
    line= rg.Line(point1,point2)
    line.thickness=10
    line.attach_to(window)
    point3 = rg.Point(200, 300)
    point4 = rg.Point(170, 250)
    line2 = rg.Line(point3, point4)
    line2.attach_to(window)
    midpoint= line.get_midpoint()
    print(midpoint)
    print(midpoint.x)
    print(midpoint.y)
    window.render()
    window.close_on_mouse_click()
# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()
