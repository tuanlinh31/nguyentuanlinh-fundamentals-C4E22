from turtle import *
speed()

shape("turtle")
for n in range(5):
    if n%2==0:
        for i in range(7-n):
            color("red")
            forward(100) 
            left(360/(7-n))
    else:
        for i in range(7-n):
            color("blue")
            forward(100) 
            left(360/(7-n))

mainloop()