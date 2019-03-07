"""
This module lets you practice  ** using objects **, including:
  -- CONSTRUCTING objects,
  -- applying METHODS to them, and
  -- accessing their DATA via INSTANCE VARIABLES

Authors: David Mutchler, Vibha Alangar, Matt Boutell, Dave Fisher, Mark Hays,
         Aaron Wilkin, their colleagues, and Lauren Copland.
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

    window = rg.RoseWindow()
    nick = rg.Circle(rg.Point(100,100),10)
    susan = rg.Circle(rg.Point(300,100),50)
    susan.fill_color = 'midnight blue'

    nick.attach_to(window)
    susan.attach_to(window)

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

    window = rg.RoseWindow()

    xc = 300
    yc = 100

    x1 = 50
    y1 = 50
    x2 = 150
    y2 = 200

    circle = rg.Circle(rg.Point(xc,yc),50)
    rectangle = rg.Rectangle(rg.Point(x1,y1), rg.Point(x2,y2))

    circle.fill_color = 'blue'

    circle.attach_to(window)
    rectangle.attach_to(window)

    window.render()
    window.close_on_mouse_click()

    print("Circle Information")
    print("     The outline thickness is", circle.outline_thickness)
    print("     The fill color is", circle.fill_color)
    print("     The center is at point", "(",xc,", ", yc,")")
    print("     The x coordinate is", xc)
    print("     The y coordiante is", yc)
    print("")
    print("Rectangle Information")
    print("     The outline thickness is", rectangle.outline_thickness)
    print("     The fill color is", rectangle.fill_color)
    print("     The center is at point", "(",(x1+(x2-x1)),", ", (y1+(y2-y1)), ")")
    print("     The x coordinate is", (x1+(x2-x1)))
    print("     The y coordiante is", (y1+(y2-y1)))
#Its outline thickness.
 #         -- Its fill color.
  #        -- Its center.
   #       -- Its center's x coordinate.
    #      -- Its center's y coordinate.

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

    window = rg.RoseWindow()
    line1 = rg.Line(rg.Point(50, 50), rg.Point(100, 50))
    line2 = rg.Line(rg.Point(50,100), rg.Point(300, 100))

    line2.thickness = 15

    print('')
    print("The midpoint of the thick line is",line2.get_midpoint())
    print("     The x coordinate of thick line's midpoint is", line2.get_midpoint().x)
    print("     The y coordinate of thick line's midpoint is", line2.get_midpoint().y)


    line1.attach_to(window)
    line2.attach_to(window)


    window.render()
    window.close_on_mouse_click()



# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()
