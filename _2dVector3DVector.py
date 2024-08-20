# Creata a class C-2d vector and use it to create another class representing 3-d vector

class C2dVec:
    def __init__(self,i,j):
        self.icap=i
        self.jcap=j
    def __str__(self):
        return f"{self.icap}i + {self.jcap}j"
    
class C3dVec(C2dVec):
    def __init__(self,i,j,k):
        super().__init__(i,j)   #don't forget to pass the arguments
        self.kcap=k
    def __str__(self):
        return f"{self.icap}i + {self.jcap}j + {self.kcap}k"

v2d=C2dVec(2,4)
print(v2d)
v3d=C3dVec(3,15,7)
print(v3d)
 