

class Vector3:
    """Vector (x, y, z) of real numbers."""

    def __init__(self, x, y, z):
        self.x = float(x)
        self.y = float(y)
        self.z = float(z)

    def __repr__(self):
        return f"Vector3({self.x}, {self.y}, {self.z})"

    def __str__(self):
        return f"({self.x:g}, {self.y:g}, {self.z:g})"

    def __add__(self, other):
        if not isinstance(other, Vector3):
            return NotImplemented
        return Vector3(self.x + other.x, self.y + other.y,
                       self.z + other.z)

    def __mul__(self, k):
        """v * k, with k a number."""
        if not isinstance(k, (int, float)):
            return NotImplemented
        return Vector3(k * self.x, k * self.y, k * self.z)

    def __rmul__(self, k):
        """k * v."""
        return self * k

    def __eq__(self, other):
        if not isinstance(other, Vector3):
            return NotImplemented
        return (self.x == other.x and self.y == other.y
                and self.z == other.z)

    def __len__(self):
        return 3

    def __getitem__(self, i):
        return (self.x, self.y, self.z)[i]

    def __iter__(self):
        return iter((self.x, self.y, self.z))
    
    def __sub__ (self, other):
        if not isinstance(other, Vector3):
            return NotImplemented
        return Vector3(self.x - other.x, self.y - other.y,
                       self.z - other.z)

    def __neg__(self, other):
        if not isinstance(other, Vector3):
            return NotImplemented
        return Vector3(-self.x, -self.y, -self.z)

    def __truediv__(self, other):
        if not isintance(other, Vector3):
            return NotImplemented
        return Vector3(self.x / other.x, self.y / other.y, self.z /other.z)

    def __matmul__(self, other):
        if not isinstance(other, Vector3):
            return NotImplemented
        return Vector3(self.x * other.x + self.y * other.y + self.z * other.z)
    



if __name__ == "__main__":
    v = Vector3(1,2,3)
    print(v)