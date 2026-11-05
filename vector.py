class Vector3: 
    """This is a cloass or a three dimensional vector"""
    def __innit__(self,xyz): 
        self.x=x
        self.y=y
        self.z=z

    def __repr__(self):
        return f"Vector3({self.x},{self.y},{self.z})"

    def __str__(self):
        return f"({self.x:g} {self.y:g} {self.z:g})"

    def __add__(self, other):
        if not instance(other,Vector3):
            return NotImplemented
        return Vector3(self.x+other.x,self.y+other.y,self.z+other.z)

    

if __name__ == "__main__":
    v = Vector3(1,2,3)
    print(v)