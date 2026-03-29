class narzym():
    def __init__(self, number):
        self.number = number
    def konwerter(self):
        self.rzymnumber = []
        while self.number!=0:
            if self.number >=1000:
                self.number =self.number -1000
                self.rzymnumber.append("M")
            elif self.number >=900:
                self.number = self.number - 900
                self.rzymnumber.append("CM")
            elif self.number >=800:
                self.number = self.number - 800
                self.rzymnumber.append("DCCC")
            elif self.number >= 700:
                self.number = self.number - 700
                self.rzymnumber.append("DCC")
            elif self.number >= 600:
                self.number = self.number -600
                self.rzymnumber.append("DC")
            elif self.number >= 500:
                self.number = self.number - 500
                self.rzymnumber.append("D")
            elif self.number >= 400:
                self.number = self.number - 400
                self.rzymnumber.append("CD")
            elif self.number >= 300:
                self.number = self.number - 300
                self.rzymnumber.append("CCC")
            elif self.number >= 200:
                self.number = self.number - 200
                self.rzymnumber.append("CC")
            elif self.number >= 100:
                self.number = self.number - 100
                self.rzymnumber.append("C")
            elif self.number >= 90:
                self.number = self.number - 90
                self.rzymnumber.append("XC")
            elif self.number >= 80:
                self.number = self.number - 80
                self.rzymnumber.append("LXXX")
            elif self.number >= 70:
                self.number = number - 70
                self.rzymnumber.append("LXX")
            elif self.number >= 60:
                self.number = self.number - 60
                self.rzymnumber.append("LX")
            elif self.number >= 50:
                self.number = self.number - 50
                self.rzymnumber.append("L")
            elif self.number >= 40:
                self.number = self.number - 40
                self.rzymnumber.append("XL")
            elif self.number >= 30:
                self.number = self.number - 30
                self.rzymnumber.append("XXX")
            elif self.number >= 20:
                self.number = self.number - 20
                self.rzymnumber.append("XX")
            elif self.number >= 10:
                self.number = self.number - 10
                self.rzymnumber.append("X")
            elif self.number >= 9:
                self.number = self.number - 9
                self.rzymnumber.append("IX")
            elif self.number >= 8:
                self.number = self.number - 8
                self.rzymnumber.append("VIII")
            elif self.number >= 7:
                self.number = self.number - 7
                self.rzymnumber.append("VII")
            elif self.number >= 6:
                self.number = self.number - 6
                self.rzymnumber.append("VI")
            elif self.number >= 5:
                self.number = self.number - 5
                self.rzymnumber.append("V")
            elif self.number >= 4:
                self.number = self.number - 4
                self.rzymnumber.append("IV")
            elif self.number >= 1:
                self.number = self.number - 1
                self.rzymnumber.append("I")
        self.rzymska = ''.join(self.rzymnumber)
        return self.rzymska
rzymskaliczba = int(input("Podaj liczbę, która zostanie zamieniona na rzymską: "))
rzymskaliczba = narzym(rzymskaliczba)
print(rzymskaliczba.konwerter())