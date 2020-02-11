from display import *
from draw import *
import random

s = new_screen()

x0 = 0
y0 = 0
x1 = 499
y1 = 499

c = [255,255,255]
draw_line(0, 250, x1, 250, s, c);
draw_line(250, 0, 250, y1, s, c);

#octants 1 and 5
c = [ 255, 255, 51]
num = 0
d = 1
draw_line(0, 0, x1, y1, s, c)
for x in range (1, 10) :
    num+=30
    draw_line(0, num, x1, y1-num, s, c)

#octants 4 and 8
c = [ 135, 206, 250]
for x in range (1,10) :
    num+=30
    draw_line(0, num, x1, y1-num, s, c)
    # draw_line(num,0,x1-num,y1,s,c)

#octants 3 and 7
c = [ 240, 116, 116]
for x in range (1,30) :
    num+=50
    draw_line(0,num,x1,y1-num,s,c)
    # draw_line(0, num, x1, y1-num, s, c)

#octants 2 and 6
c = [116, 240, 149]
num = 0
for x in range (1, 20) :
    num-=30
    draw_line(0, num, x1, y1-num, s, c)

display(s)
save_ppm(s, 'binary.ppm')
save_ppm_ascii(s, 'ascii.ppm')
save_extension(s, 'img.png')
