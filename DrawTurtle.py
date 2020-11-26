from turtle import *
from math import sqrt
t = Turtle()
s = Screen()
A4 = [210, 297]
turtle_img = [[305, 160], [315, 160], [325, 160], [325, 150], [325, 140], [325, 130], [325, 120], [335, 120], [335, 130],
         [335, 140], [345, 140], [345, 150], [355, 150], [365, 150], [375, 150], [385, 150], [385, 140], [395, 140],
         [395, 130], [395, 120], [395, 110], [385, 110], [385, 100], [375, 100], [375, 110], [365, 110], [355, 110],
         [345, 110], [335, 110], [335, 100], [325, 100], [325, 110], [315, 110], [315, 120], [315, 130], [315, 140],
         [305, 140], [305, 150], [305, 160]]
ship = [[305, 160], [315, 160], [315, 150], [325, 150], [325, 140], [335, 140], [335, 130], [345, 130], [345, 120],
        [345, 110], [345, 100], [335, 100], [325, 100], [315, 100], [315, 90], [325, 90], [335, 90], [345, 90],
        [355, 90], [365, 90], [365, 80], [355, 80], [355, 70], [345, 70], [345, 60], [335, 60], [325, 60], [315, 60],
        [305, 60], [295, 60], [285, 60], [275, 60], [275, 70], [265, 70], [265, 80], [255, 80], [255, 90], [265, 90],
        [275, 90], [285, 90], [295, 90], [305, 90], [305, 100], [305, 110], [305, 120], [305, 130], [305, 140],
        [305, 150], [305, 160]]
images = [turtle_img, ship]

robot_displace = (-220, -20)
notebook = 1000, 1000
count = 4
n = round(sqrt(count))
window_size = [A4[0], A4[1]]
t.speed(20)
s.screensize(canvheight=notebook[0], canvwidth=notebook[1], bg="white")
print(s.screensize())



t.penup()
t.goto(0, 0)


def draw_paper(corner=robot_displace, paper=A4):
    t.penup()
    cx, cy = corner
    px, py = paper
    t.goto(corner)
    t.pendown()
    t.goto(cx + px, cy)
    t.goto(cx + px, cy + py)
    t.goto(cx, cy + py)
    t.goto(cx, cy)
    t.penup()


def draw_image(image, displace=robot_displace):
    t.penup()
    dx, dy = displace[0] + robot_displace[0], displace[1] + robot_displace[1]
    t.goto(image[0][0] + dx, image[0][1] + dy)
    t.pendown()
    for i in image:
        t.goto(i[0] + dx, i[1] + dy)
    t.penup()


for i in range(len(images)):
    draw_paper(corner=(A4[0] * i, 0))
    draw_image(image=images[i], displace=(A4[0] * i, 0))
s.exitonclick()
