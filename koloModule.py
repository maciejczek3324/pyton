class kolo():
    def __init__(self, promien):
        import math
        self.promien = promien
        self.PI = math.pi
    def pole(self):
        import math
        p = ((math.pow(self.promien,2))*self.PI)
        return p
    def obw(self):
        obw = 2*self.PI*self.promien
        return obw