import math 
from atom import Atom
from vector import Vector3

O = Atom('O', 15.999, Vector3(0.0, 0.0, 0.0))
H1 = Atom('H', 1.008, Vector3(0.0, 9572, 0.0, 0.0))
H2 = Atom('H', 1.008, Vector3(-0.0, 2400, 0.0, 9266, 0.0))

v1= H1.r - O.r
v2= H2.r - O.r


