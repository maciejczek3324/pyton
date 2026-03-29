import math
class kolo():
    def __init__(self, promien):
        self.promien = promien
        self.PI = math.pi
    def pole(self):
        p = ((math.pow(self.promien,2))*self.PI)
        return p
    def obw(self):
        obw = 2*self.PI*self.promien
        return obw
class walec(kolo):
    def __init__(self,promien,wysokosc):
        super().__init__(promien)
        self.wysokosc = wysokosc
        self.PI = math.pi
    def polecal(self):
        polecal = (2*(math.pow(self.promien,2))*self.PI) + (2*self.PI*self.promien*self.wysokosc)
        return polecal
    def obj(self):
        obj = ((math.pow(self.promien,2))*self.PI) * self.wysokosc
        return obj

print("Witaj w programie obliczającym obwód koła, pole koła, oraz pole i objętość walca.Program pozwoli Ci wybrać co chcesz obliczyć po tym będziesz musiał podać nam potrzebne dane.")
print("Aby obliczyć pole koła wcisnij 1.\n"
      "Aby obliczyć obówd koła wcisnij 2.\n"
      "Aby obliczyć pole powierzchni całkowitej walca wciśnij 3.\n"
      "Aby obliczyc objętość walca wciśnij 4.")
wybor = int(input("Jakie obliczenie wybierasz: "))
if wybor == 1:
    r = int(input("Podaj promien koła: "))
    prom = kolo(r)
    print("Pole koła wynosi: " + str(prom.pole()))
elif wybor == 2:
    r = int(input("Podaj promien koła: "))
    prom = kolo(r)
    print("Obwód koła wynosi: " + str(prom.obw()))
elif wybor == 3:
    r = int(input("Podaj promien walca: "))
    h = int(input("Podaj wysokosc walca: "))
    wys = walec(r, h)
    print("Pole powierzchni całkowitej walca wynosi: " + str(wys.polecal()))
elif wybor ==4:
    r = int(input("Podaj promien walca: "))
    h = int(input("Podaj wysokosc walca: "))
    wys = walec(r, h)
    print("Objętość walca wynosi: " + str(wys.obj()))