decNumbers=[523, 458, 399, 878, 1001, 1112, 2056]
binNumbers=[]
octNumbers=[]
hexNumbers=[]
for x in decNumbers:
   wynik =0
   i=1
   bin=[]
   while x !=0:
       bin.append(x%2)
       x=int(x/2)
   for y in range(0,len(bin)):
       wynik+=bin[y] *i
       i=i*10
   binNumbers.append(wynik)

for x in decNumbers:
    wynik =0
    i=1
    okt=[]
    while x!=0:
        okt.append(x%8)
        x=int(x/8)
    for y in range(0,len(okt)):
        wynik+=okt[y]*i
        i=i*10
    octNumbers.append(wynik)

for x in decNumbers:
    wynik = 0
    i=1
    heks=[]
    while x!=0:
        heks.append(x%16)
        x=int(x/16)
    heks.reverse()
    for y in range(0,len(heks)):
        if heks[y]==10:
            heks[y]='A'
        if heks[y]==11:
            heks[y]='B'
        if heks[y]==12:
            heks[y]='C'
        if heks[y]==13:
            heks[y]='D'
        if heks[y]==14:
            heks[y]='E'
        if heks[y]==15:
            heks[y]='F'
    for y in range(0, len(heks)):
        wynik=str(wynik)+str(heks[y])
    hexNumbers.append(wynik)

print("Liczby "+str(decNumbers)+" zapisane w systemie dwójkowym to "+str(binNumbers))
print("Liczby "+str(decNumbers)+" zapisane w systemie ósemkowym to "+str(octNumbers))
print("Liczby "+str(decNumbers)+" zapisane w systemie szesnastkowym to "+str(hexNumbers))