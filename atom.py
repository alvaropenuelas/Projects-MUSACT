from dataclasses import dataclass

from vector import Vector3


@dataclass
class Atom:
    """Atom with mass in u and position in angstroms."""

    symbol: str
    mass: float
    r: Vector3
