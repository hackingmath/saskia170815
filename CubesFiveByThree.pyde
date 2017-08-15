'''Cloning another Saskia sketch:
https://twitter.com/sasj_nl/status/897524484835594240
August 15, 2017'''

cubeList = []

class Cube:
    def __init__(self,x,y,row,col):
        self.x = x
        self.y = y
        self.z = 10
        self.row = row
        self.col = col
        self.ang = 0
        self.sz = 100
        self.c = color(20*(row+1)*(col+1),300,300)
        
    def update(self):
        strokeWeight(3)
        stroke(255,0,255)#pink
        pushMatrix()
        translate(self.x,self.y,self.z)
        stroke(self.c)
        if (self.row + self.col) % 2 == 0:
            rotateY(sin(.05*t))
            box(60+30*sin(.05*t))
        else:
            rotateY(-sin(.05*t))
            box(60-30*sin(.05*t))
        popMatrix()

t = 0 #time
dt = 0.5 #change in time

def setup():
    size(600,600, P3D)
    colorMode(HSB)
    noFill()
    for row in range(5):
        for col in range(3):
            cubeList.append(Cube(100*col,100*row,row,col))
            
def draw():
    global t, dt
    background(255)#white
    translate(200,100,-100)
    for cube in cubeList:
        cube.update()
    t += dt
            