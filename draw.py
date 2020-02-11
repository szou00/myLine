#received help from Bernard, who explained the outline of the code
from display import *

def draw_line( x0, y0, x1, y1, screen, color ):

    #changing values that would be in octant 3,4,5,6 to match 1,2,7,8
    if x0 > x1:
        x0, x1, y0, y1 = x1, x0, y1, y0

    current_x = x0
    current_y = y0

    A = y1 - y0
    B = -1 * (x1 - x0)

    if current_x < x1:
        m = -1 * float(A) / float(B)
        #if in octant 1
        if m <= 1 and m >= 0:
            d = (2 * A) + B
            while current_x <= x1:
                plot(screen, color, current_x, current_y)
                #if it's above the midpoint
                if d > 0:
                    current_y += 1
                    d += 2 * B
                current_x += 1
                d += 2 * A

        elif m > 1:
            d = A + (2 * B)
            while current_y <= y1:
                plot(screen, color, current_x, current_y)
                #if it's below the midpoint
                if d < 0:
                    current_x += 1
                    d += 2 * A
                current_y += 1
                d += 2 * B

        elif m <= 0 and m >= -1:
            d = (2 * A) + B
            while current_x <= x1:
                plot(screen, color, current_x, current_y)
                if d < 0:
                    current_y -= 1
                    d -= 2 * B
                current_x += 1
                d += 2 * A

        elif m <= -1:
            d = A - (2 * B)
            while current_y >= y1:
                plot(screen, color, current_x, current_y)
                if d > 0:
                    current_x += 1
                    d += 2 * A
                current_y -= 1
                d -= 2 * B

    else:
        if current_y < y1:
            while current_y < y1:
                plot(screen, color, current_x, current_y)
                current_y += 1
        else:
            while current_y > y1:
                plot(screen, color, current_x, current_y)
                current_y -= 1
