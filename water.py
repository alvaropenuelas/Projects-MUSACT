import math 
from atom import Atom
from vector import Vector3

O = Atom('O', 15.999, Vector3(0.0, 0.0, 0.0))
H1 = Atom('H', 1.008, Vector3(0.9572, 0.0, 0.0))
H2 = Atom('H', 1.008, Vector3(-0.2400, 0.9266, 0.0))

v1 = H1.r - O.r
v2 = H2.r - O.r

d_OH1 = abs(v1)
d_OH2 = abs(v2)
angle = math.degrees(math.acos((v1 @ v2) / (d_OH1 * d_OH2)))

total_mass = O.mass + H1.mass + H2.mass
center_of_mass = (
    O.mass * O.r + H1.mass * H1.r + H2.mass * H2.r
) / total_mass

print(f"Distancia O-H1: {d_OH1:.4f} Å")
print(f"Distancia O-H2: {d_OH2:.4f} Å")
print(f"Ángulo H-O-H: {angle:.2f}°")
print(f"Centro de masas: {center_of_mass} Å")
