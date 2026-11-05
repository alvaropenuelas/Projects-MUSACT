"""Pair potentials: a common interface and Lennard-Jones.

Truncated and shifted Lennard-Jones, in reduced units:

    V(r) = 4 [(1/r)^12 - (1/r)^6] - V_c   if r < rc,   0 if r >= rc

where V_c is the value of the unshifted potential at rc. Periodic cubic
box of side L, with the minimum image convention.
"""
from abc import ABC, abstractmethod

import numpy as np


class Potential(ABC):
    """Common interface for pair potentials."""

    @abstractmethod
    def forces(self, x: np.ndarray,
               L: float) -> tuple[float, np.ndarray]:
        """Potential energy and forces (n, 3)."""


class LennardJones(Potential):
    """Lennard-Jones truncated and shifted at rc."""

    def __init__(self, rc: float = 2.5) -> None:
        if rc <= 0:
            raise ValueError("the cutoff radius must be positive")
        self.rc = rc
        s6 = 1.0 / rc**6
        self.vc = 4.0 * (s6 * s6 - s6)

    def __repr__(self) -> str:
        return f"LennardJones(rc={self.rc})"

    def forces(self, x: np.ndarray,
               L: float) -> tuple[float, np.ndarray]:
        if self.rc > 0.5 * L:
            raise ValueError("minimum image: rc > L/2")
        d = x[:, None, :] - x[None, :, :]  # x[i] - x[j]
        d -= L * np.rint(d / L)  # minimum image
        r2 = np.sum(d * d, axis=2)
        np.fill_diagonal(r2, np.inf)
        inside = r2 < self.rc**2
        inv2 = np.where(inside, 1.0 / r2, 0.0)
        s6 = inv2**3
        v = 4.0 * (s6 * s6 - s6) - self.vc
        epot = 0.5 * float(np.sum(v[inside]))
        fr = 24.0 * inv2 * (2.0 * s6 * s6 - s6)
        f = np.sum(fr[:, :, None] * d, axis=1)
        return epot, f

if __name__ == "__main__":
    s = LennardJones()