# ISC License

# Copyright (c) 2024 James Osborn

# Permission to use, copy, modify, and/or distribute this software for any purpose 
# with or without fee is hereby granted, provided that the above copyright notice 
# and this permission notice appear in all copies.

# THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES WITH 
# REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF MERCHANTABILITY 
# AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY SPECIAL, DIRECT, 
# INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES WHATSOEVER RESULTING FROM 
# LOSS OF USE, DATA OR PROFITS, WHETHER IN AN ACTION OF CONTRACT, NEGLIGENCE 
# OR OTHER TORTIOUS ACTION, ARISING OUT OF OR IN CONNECTION WITH THE USE OR 
# PERFORMANCE OF THIS SOFTWARE.

from turtle import Screen, Turtle
import math
import sys
screen = Screen()
screen.setup(width=1.0, height=1.0)  # Set the screen to full-screen mode
screen.tracer(True)
turtle = Turtle(visible=True)
global length
length = 5
global halflength
halflength = length * 0.5

def north():
    turtle.setheading(90) # North
    

def ne():
    turtle.setheading(60) # Northeast
    

def nw():
    turtle.setheading(120) # Northwest
    

def east():
    turtle.setheading(0) # East
    

def west():
    turtle.setheading(180) # West
    
def south():
    turtle.setheading(270) # South
    

def se():
    turtle.setheading(-60) # Southeast
    

def sw():
    turtle.setheading(-120) # Southwest

def halftopeast():
    turtle.setheading(-30)
    full()
    
def pointytopwest():
    turtle.setheading(150)
    full()
    turtle.setheading(210)
    full()

def pointytopeast():
    turtle.setheading(30)
    full()
    turtle.setheading(-30)
    full()

def pointybasewest():
    turtle.setheading(210)
    full()
    turtle.setheading(150)
    full()

def pointybaseeast():    
    turtle.setheading(-30)
    full()
    turtle.setheading(30)
    full()

def hexbreak():
    print("Hello World!")

def full():
    turtle.forward(50)

def done():
    screen.exitonclick()

def hexsecond(): # This function draws the right half of each hexagon, in each column of the left half of the grid
    west()
    half()
    nw()
    full()
    ne()
    full()
    east()
    half()

def hexthird():

    west()
    half()
    sw()
    full()
    se()
    full()
    east()
    half()

def hexfourth():
    east()
    half()
    ne()
    full()
    nw()
    full()
    west()
    half()

def stepdownleft(): # This function steps down to the next left column of hexagons.
    west()
    half()
    sw()
    full()
    west()
    half()

def stepdownright(): # This function steps down to the next right column of hexagons.
    east()
    half()
    se()
    full()
    east()
    half()

def leftback():
    turtle.penup()
    turtle.goto(-20,400)
    turtle.pendown()
    half()
    se()
    full()
    east()
    half()

def leftcleanup():
    turtle.pen(pencolor="white")
    east()
    half()
    turtle.pen(pencolor="black")

def rightcleanup():
    turtle.pen(pencolor="white")
    west()
    half()
    turtle.pen(pencolor="black")
    turtle.penup()
    turtle.goto(-20,400)
    east()
