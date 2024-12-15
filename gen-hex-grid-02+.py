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

import bpy
import numpy

ystack = [0]
xstack = [0]

def half_length_down():
    global ystack
    a = ystack.pop(0)
    offset = numpy.add(a, 0.866)
    print(offset)  # Print the result to the console
    ystack.insert(0, offset)

def half_length_up():
    global ystack
    a = ystack.pop(0)
    offset = numpy.add(a, -0.866)
    print(offset)  # Print the result to the console
    ystack.insert(0, offset)

def full_length_down():
    global ystack
    a = ystack.pop(0)
    offset = numpy.add(a, 1.732)
    print(offset)  # Print the result to the console
    ystack.insert(0, offset)

def full_length_up():
    global ystack
    a = ystack.pop(0)
    offset = numpy.add(a, -1.732)
    print(offset)  # Print the result to the console
    ystack.insert(0, offset)

def right():
    global xstack
    a = xstack.pop(0)
    offset = numpy.add(a, 1.5)
    print(offset)  # Print the result to the console
    xstack.insert(0, offset)

def left():
    global xstack
    a = xstack.pop(0)
    offset = numpy.add(a, -1.5)
    print(offset)  # Print the result to the console
    xstack.insert(0, offset)

def render_hexagon():
    global ystack
    global xstack
    y = ystack[-1]
    x = xstack[-1]
    loc = y, x, 0
    bpy.ops.mesh.primitive_cylinder_add(
    vertices=6,
    radius=1,
    depth=0.25,
    location=(loc)
)

def onedown():
    global hexdic
    rstack = [3, 7]
    while len(rstack) > 0:
        num = rstack.pop(0)
        hexdic[num]()

def twodown():
    global hexdic
    rstack = [8, 8]
    while len(rstack) > 0:
        num = rstack.pop(0)
        hexdic[num]()

def fourdown():
    global hexdic
    rstack = [9, 9]
    while len(rstack) > 0:
        num = rstack.pop(0)
        hexdic[num]()

def onedownright():
    global hexdic
    rstack = [1, 5, 7]
    while len(rstack) > 0:
        num = rstack.pop(0)
        hexdic[num]()

def twodownright():
    global hexdic
    rstack = [11, 11]
    while len(rstack) > 0:
        num = rstack.pop(0)
        hexdic[num]()

def fourdownright():
    global hexdic
    rstack = [12, 12]
    while len(rstack) > 0:
        num = rstack.pop(0)
        hexdic[num]()

def onedownleft():
    global hexdic
    rstack = [1, 6, 7]
    while len(rstack) > 0:
        num = rstack.pop(0)
        hexdic[num]()
        
def twodownleft():
    global hexdic
    rstack = [14, 14]
    while len(rstack) > 0:
        num = rstack.pop(0)
        hexdic[num]()

def fourdownleft():
    global hexdic
    rstack = [15, 15]
    while len(rstack) > 0:
        num = rstack.pop(0)
        hexdic[num]()

def oneupright():
    global hexdic
    rstack = [2, 5, 7]
    while len(rstack) > 0:
        num = rstack.pop(0)
        hexdic[num]()
        
def twoupright():
    global hexdic
    rstack = [17, 17]
    while len(rstack) > 0:
        num = rstack.pop(0)
        hexdic[num]()

def fourupright():
    global hexdic
    rstack = [18, 18]
    while len(rstack) > 0:
        num = rstack.pop(0)
        hexdic[num]()

def oneupleft():
    global hexdic
    rstack = [2, 6, 7]
    while len(rstack) > 0:
        num = rstack.pop(0)
        hexdic[num]()

def twoupleft():
    global hexdic
    rstack = [20, 20]
    while len(rstack) > 0:
        num = rstack.pop(0)
        hexdic[num]()
        
def fourupleft():
    global hexdic
    rstack = [21, 21]
    while len(rstack) > 0:
        num = rstack.pop(0)
        hexdic[num]()
        
def firstfive():
    global hexdic
    rstack = [7, 11, 14, 20]
    while len(rstack) > 0:
        num = rstack.pop(0)
        hexdic[num]()

def secondline():
    global hexdic
    rstack = [14, 12, 18]
    while len(rstack) > 0:
        num = rstack.pop(0)
        hexdic[num]()
        
def thirdline():
    global hexdic
    rstack = [11, 14, 15, 21, 20]
    while len(rstack) > 0:
        num = rstack.pop(0)
        hexdic[num]()

def fourthline():
    global hexdic
    rstack = [14, 13, 19]
    while len(rstack) > 0:
        num = rstack.pop(0)
        hexdic[num]()
        
def fifthline():
    global hexdic
    rstack = [11, 14, 16, 20, 22]
    while len(rstack) > 0:
        num = rstack.pop(0)
        hexdic[num]()

def sixthline():
    global hexdic
    rstack = [8, 13, 11, 17, 19]
    while len(rstack) > 0:
        num = rstack.pop(0)
        hexdic[num]()

def top():
    global hexdic
    rstack = [23, 24, 25, 26, 27]
    while len(rstack) > 0:
        num = rstack.pop(0)
        hexdic[num]()

def seventhline():
    global hexdic
    rstack = [8, 14, 16, 20, 22]
    while len(rstack) > 0:
        num = rstack.pop(0)
        hexdic[num]()

hexdic = {
    1: half_length_down,
    2: half_length_up,
    3: full_length_down,
    4: full_length_up,
    5: right,
    6: left,
    7: render_hexagon,
    8: onedown,
    9: twodown,
    10: fourdown,
    11: onedownright,
    12: twodownright,
    13: fourdownright,
    14: onedownleft,
    15: twodownleft,
    16: fourdownleft,
    17: oneupright,
    18: twoupright,
    19: fourupright,
    20: oneupleft,
    21: twoupleft,
    22: fourupleft,
    23: firstfive,
    24: secondline,
    25: thirdline,
    26: fourthline,
    27: fifthline,
    28: sixthline,
    29: top,
    30: seventhline
}

def hexloop():
    global hexdic
    rstack = [29, 28, 30, 28, 30, 28]
    while len(rstack) > 0:
        num = rstack.pop(0)
        hexdic[num]()
                
hexloop()
