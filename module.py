from koloModule import kolo
from kulaModule import kula
print("Witaj w programie obliczającym obwód koła, pole koła, oraz pole i objętość walca.Program pozwoli Ci wybrać co chcesz obliczyć po tym będziesz musiał podać nam potrzebne dane.")
print("Aby obliczyć pole koła wcisnij 1.\n"
      "Aby obliczyć obówd koła wcisnij 2.\n"
      "Aby obliczyć pole powierzchni całkowitej kuli wciśnij 3.\n"
      "Aby obliczyc objętość kuli wciśnij 4.")
wybor = int(input("Jakie obliczenie wybierasz: "))
if wybor == 1:
    r = int(input("Podaj promien koła: "))
    prom = kolo(r)
    print("Pole koła wynosi: " + str(prom.pole()))
elif wybor == 2:
    r = int(input("Podaj promien koła: "))
    prom = kolo(r)
    print("Obwód koła wynosi: " + str(prom.obw()))
elif wybor == 2:
    r = int(input("Podaj promien koła: "))
    prom = kolo(r)
    print("Obwód koła wynosi: " + str(prom.obw()))
elif wybor == 3:
    r = int(input("Podaj promien kuli:"))
    wys= kula(r)
    print("Pole powierzchni całkowitej kuli wynosi: " + str(wys.polecal()))
elif wybor ==4:
    r = int(input("Podaj promien kuli: "))
    wys=kula(r)
    print("Objętość kuli wynosi: " + str(wys.obj()))