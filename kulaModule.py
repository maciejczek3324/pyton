from koloModule import kolo
class kula(kolo):
    def __init__(self,promien):
        import math
        super().__init__(promien)
        self.PI = math.pi
    def polecal(self):
        import math
        polecal = 4*self.PI * self.promien**2
        return polecal
    def obj(self):
        import math
        obj = 4/3*self.PI*self.promien**3
        return obj