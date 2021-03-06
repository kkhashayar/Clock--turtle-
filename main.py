import turtle, time,random ##winsound

distance = 20
width = 6
height = 11

screen = turtle.Screen()
screen.setup(600,600,700)
screen.bgcolor("black")
screen.title("K-clock v.1")
screen.tracer(0)

colors = ["white","yellow","green","red","blue","gray","orange"]

sec = 0
minute = 0

font = ("arial", "30", "bold")
p = turtle.Turtle()
p.setpos(-100, 0)
p.hideturtle()
p.pencolor("yellow")

p2 = turtle.Turtle()
p2.setpos(-40, 0)
p2.hideturtle()
p2.pencolor("orange")

class Player(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.penup()
        self.pencolor("red")
        self.shape("square")
        self.shapesize(1)
        self.fillcolor("red")
        self.speed(0)
        self.speed = distance
        self.setheading(0)
        self.setpos(positions_s[0])

    def update_sec(self):
        global sec
        if sec == 60:
            sec= 0
            self.setpos(positions_s[0])
            text.draw()
            #winsound.Beep(2000,45)

        if sec < 60:
            sec+=1
            ##winsound.Beep(200,40)
            ################################################
            p.clear()
            p.write(sec, font=font)
            clock_s()
            ################################################
            self.setpos(positions_s[sec])
            self.fillcolor(random.choice(colors))
            time.sleep(1)

    def update_minute(self):
        global minute
        if minute == 59:
            minute= 0
            self.setpos(positions_m[0])

        if minute < 60:
            minute+=1
            ################################################
            p2.clear()
            p2.write(minute, font=font)
            clock_m()
            ################################################
            self.setpos(positions_m[minute])
            self.fillcolor(random.choice(colors))



class Pen(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.penup()
        self.pencolor("yellow")
        self.shape("square")
        self.shapesize(1)
        self.fillcolor("black")
        self.speed(0)
        self.setpos(-260, 260)

################################################
p.write(sec, font=font)
################################################
pen = Pen()
positions_s = []
positions_m = []

for i in range(height):
    for i in range(width):
        pen.stamp()
        positions_s.append(pen.pos())
        pen.forward(distance)
    pen.back(distance * width)
    pen.right(90)
    pen.forward(distance)
    pen.left(90)

pen_2 = Pen()
pen_2.setpos(-260,0)
for i in range(height):
    for i in range(width):
        pen.stamp()
        positions_m.append(pen.pos())
        pen.forward(distance)
    pen.back(distance * width)
    pen.right(90)
    pen.forward(distance)
    pen.left(90)


player_s = Player()
player_m = Player()

circle2 = turtle.Turtle()
circle2.penup()
circle2.speed(0)
circle2.pencolor("green")
circle2.setpos(150,150)
circle2.pendown()
circle2.pensize(1)
circle2.circle(50)
circle2.hideturtle()

circle = turtle.Turtle()
circle.penup()
circle.speed(0)
circle.pencolor("red")
circle.setpos(150,150)
circle.pendown()
circle.pensize(1)
circle.circle(50)
circle.hideturtle()
circle.setheading(90)
circle.penup()
circle.forward(50)

circle3 = turtle.Turtle()
circle3.penup()
circle3.speed(0)
circle3.pencolor("red")
circle3.setpos(150,150)
circle3.pendown()
circle3.pensize(1)
circle3.circle(50)
circle3.hideturtle()
circle3.setheading(90)
circle3.penup()
circle3.forward(50)

def clock_m():
    circle3.penup()
    circle3.clear()
    circle3.pendown()
    circle3.pensize(2)
    circle3.forward(45)
    circle3.penup()
    circle3.back(45)
    circle3.right(6)


def clock_s():
    circle.penup()
    circle.clear()
    circle.pendown()
    circle.pensize(2)
    circle.forward(50)
    circle.penup()
    circle.back(50)
    circle.right(6)

clock_s()
clock_m()
#t = datetime.datetime.time(datetime.datetime.now())

font_1 = ("arial", "20", "bold")

class Text(turtle.Turtle):
    def __init__ (self):
        turtle.Turtle.__init__(self)
        self.penup()
        self.color(random.choice(colors))
        self.hideturtle()
        self.setpos(-120,100)

    def draw(self):
        self.clear()
        self.color(random.choice(colors))
        self.write(time.ctime(), font = font_1)

text = Text()
while True:
    screen.update()
    player_s.update_sec()
    if sec == 60:
        player_m.update_minute()
