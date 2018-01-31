import turtle
divide = turtle.Turtle()

def square():
    for i in range(4):
        divide.forward(x)
        divide.right(360/4)
        
def triangle():
    for i in range(3):
        divide.forward(x)
        divide.right(360/3)

def pentagon():
    for i in range(5):
        divide.forward(x)
        divide.right(360/5)

def hexagon():
    for i in range(6):
        divide.forward(x)
        divide.right(360/6)

def nonagon():
    for i in range (9):
        divide.forward(x)
        divide.right(360/9)

def decagon():
    for i in range(10):
        divide.forward(x)
        divide.right(360/10)
        
y = int(input('Enter how many sides: '))
x = int(input('Enter the side length: '))
print ('I will draw a polygn with ' + str(y) + ' sides and a length of ' +str(x))

def AnyRegPoly(x,y):
    for i in range(y):
        divide.forward(x)
        divide.right(360/y)

AnyRegPoly(x,y)




    
   
    
