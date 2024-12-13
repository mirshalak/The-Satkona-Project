# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# 
#     http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import sys
import math
import turtle
from hexfunctions import *
sys.setrecursionlimit(2000)
turtle.speed(0)
turtle.penup()
turtle.goto(-400,300)
turtle.pendown()

def rightdown():
    global hex_primitives
    rstack = [4, 9, 7, 9, 8, 9]
    while len(rstack) > 0:
        num = rstack.pop(0)
        hex_primitives[num]()

def leftdown():
    global hex_primitives
    rstack = [5, 9, 8, 9, 7, 9]
    while len(rstack) > 0:
        num = rstack.pop(0)
        hex_primitives[num]()

def twohexdown():
    global hex_composites
    rstack = [1, 2]
    while len(rstack) > 0:
        num = rstack.pop(0)
        hex_composites[num]()

def twohexup():
    global hex_composites
    rstack = [4, 3]
    while len(rstack) > 0:
        num = rstack.pop(0)
        hex_composites[num]()

def twohex():
    global hex_composites
    rstack = [10, 12]
    while len(rstack) > 0:
        num = rstack.pop(0)
        hex_composites[num]()

def fourhexdown():
    global hex_composites
    rstack = [10, 10]
    while len(rstack) > 0:
        num = rstack.pop(0)
        hex_composites[num]()

def fourhexup():
    global hex_composites
    rstack = [12, 12]
    while len(rstack) > 0:
        num = rstack.pop(0)
        hex_composites[num]()

def fourhex():
    global hex_composites
    rstack = [18, 18]
    while len(rstack) > 0:
        num = rstack.pop(0)
        hex_composites[num]()

def eighthexdown():
    global hex_composites
    rstack = [11, 11]
    while len(rstack) > 0:
        num = rstack.pop(0)
        hex_composites[num]()

def eighthexup():
    global hex_composites
    rstack = [13, 13]
    while len(rstack) > 0:
        num = rstack.pop(0)
        hex_composites[num]()

def leftup():
    global hex_primitives
    rstack = [4, 9, 2, 9, 3, 9]
    while len(rstack) > 0:
        num = rstack.pop(0)
        hex_primitives[num]()

def rightup():
    global hex_primitives
    rstack = [5, 9, 3, 9, 2, 9]
    while len(rstack) > 0:
        num = rstack.pop(0)
        hex_primitives[num]()

def sixhexdown():
    global hex_composites
    rstack = [11, 10]
    while len(rstack) > 0:
        num = rstack.pop(0)
        hex_composites[num]()

def sixhexup():
    global hex_composites
    rstack = [12, 13]
    while len(rstack) > 0:
        num = rstack.pop(0)
        hex_composites[num]()

def sixhex():
    global hex_composites
    rstack = [5, 6]
    while len(rstack) > 0:
        num = rstack.pop(0)
        hex_composites[num]()

def sevenhex():
    global hex_composites
    rstack = [11, 10, 1, 3, 12, 13]
    while len(rstack) > 0:
        num = rstack.pop(0)
        hex_composites[num]()

def eighthex():
    global hex_composites
    rstack = [5, 10, 6, 12]
    while len(rstack) > 0:
        num = rstack.pop(0)
        hex_composites[num]()

def ninehex():
    global hex_composites
    rstack = [11, 11, 1, 3, 13, 13]
    while len(rstack) > 0:
        num = rstack.pop(0)
        hex_composites[num]()

def tenhex():
    global hex_composites
    rstack = [11, 11, 10, 13, 13, 12]
    while len(rstack) > 0:
        num = rstack.pop(0)
        hex_composites[num]()

def elevenhex():
    global hex_composites
    rstack = [11, 11, 10, 1, 3, 12, 13, 13]
    while len(rstack) > 0:
        num = rstack.pop(0)
        hex_composites[num]()

def upnextrow():
    global hex_primitives
    rstack = [4, 9, 2, 9]
    while len(rstack) > 0:
        num = rstack.pop(0)
        hex_primitives[num]()

def downnextrow():
    global hex_primitives
    rstack = [4, 9, 7, 9]
    while len(rstack) > 0:
        num = rstack.pop(0)
        hex_primitives[num]()

def mainloop():
    global hex_composites
    rstack = [7, 8, 14, 8, 15, 8, 16, 8, 17, 8, 22, 23, 17, 23, 16, 23, 15, 23, 14, 23, 7]
    while len(rstack) > 0:
        num = rstack.pop(0)
        hex_composites[num]()

hex_primitives = {
	1: north,
    2: ne,
	3: nw,
    4: east,
    5: west,
    6: south,
    7: se,
    8: sw,
    9: full
}

hex_composites = {
	1: rightdown,
    2: leftdown,
    3: rightup,
    4: leftup,
    5: sixhexdown,
    6: sixhexup,
    7: sixhex,
    8: upnextrow,
    9: mainloop,
    10: twohexdown,
    11: fourhexdown,
    12: twohexup,
    13: fourhexup,
    14: sevenhex,
    15: eighthex,
    16: ninehex,
    17: tenhex,
    18: twohex,
    19: fourhex,
    20: eighthexdown,
    21: eighthexup,
    22: elevenhex,
    23: downnextrow
}

mainloop()
done()
