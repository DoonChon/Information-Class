import turtle as T
from PIL import Image

img = Image.open('./Test1.jpg').convert('RGB')

RGB = []
Base_N = 10

def get_RGB(target, result_list, pn):
    for y in range(0,target.size[1], pn):
        for x in range(0, target.size[0],pn):
            r,g,b = target.getpixel((x,y))
            result_list.append([r,g,b])

def Draw(A):
    for i in range(4):
        T.fd(A)
        T.right(90)

get_RGB(img, RGB, Base_N)

Size_X = int(img.size[0]/Base_N)
Size_Y = int(img.size[1]/Base_N)

if img.size[0] % Base_N != 0:
    Size_X +=1
if img.size[1] % Base_N != 0:
    Size_Y +=1

T.colormode(255)
i = 0
T.speed(0)
offset_X = -200
offset_Y = -200

for y in range(Size_Y, 0, -1):
    for x in range(0, Size_X):
        T.penup()
        T.goto(x * Base_N+offset_X, y * Base_N+offset_Y)
        T.pendown()
        T.fillcolor(RGB[i][0], RGB[i][1], RGB[i][2])
        T.beginfill()
        Draw(Base_N)
        T.end_fill()
        i +=1
mainloop()
