import math
def podawanie_danych():
    print("Podaj współrzędne pierwszego punktu odcinka, najpierw współrzędna X potem Y")
    x1 = int(input("Podaj współrzędną X:"))
    y1 = int(input("Podaj współrzędną Y:"))
    print("Podaj współrzędne drugiego punktu odcinka, najpierw współrzędna X potem Y")
    x2 = int(input("Podaj współrzędną X:"))
    y2 = int(input("Podaj współrzędną Y:"))
    print("Podaj współrzędne punktu, najpierw współrzędna X potem Y i sprawdzimy jak punkt leży względem odcinka")
    xpkt = int(input("Podaj współrzędną X:"))
    ypkt = int(input("Podaj współrzędną Y:"))
    liczenie(x1,y1,x2,y2,xpkt,ypkt)
    return
def liczenie(x1,y1,x2,y2,xpkt,ypkt):
    if x1 == x2 and y1 == y2:
        print("nie istnieje taki odcinek")
        return
    elif (x1*y2*1)+(x2*ypkt*1)+(xpkt*y1*1)-(x2*y1*1)-(x1*ypkt*1)-(xpkt*y2*1) == 0:
        print("Punkt lezy na odcinku")
        return
    else:
        print("Punkt nie leży na odcinku, jego odległosc od odcinka to:")
        odl1 = math.fabs((xpkt*(y2-y1))+(ypkt*(x1-x2))+((x2*y1)-(x1+y2)))
        odl2 = math.sqrt(((x2 - x1)*(x2-x1)) + ((y2 - y1)*(y2-y1)))
        odleglosc = odl1/odl2
        print(odleglosc)
        return
podawanie_danych()