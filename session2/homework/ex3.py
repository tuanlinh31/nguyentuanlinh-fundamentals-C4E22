from turtle import *
speed(0)

shape("turtle")
for n in range(4):
    if n%2==0:
        for i in range(6-n):
            color("red")
            forward(100) 
            left(360/(6-n))
    else:
        for i in range(6-n):
            color("blue")
            forward(100) 
            left(360/(6-n))

mainloop()