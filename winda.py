wzrost=0
waga=0
wagawindy=900
wagi=[52,52,52,27,27,27,27,102,102,78,78,78,78,64,64,64,64,64,47,47,47,92,92,92,92]
wzrosty=[160,160,158,125,125,125,125,180,180,172,172,172,172,160,160,160,170,170,150,150,150,179,179,179,179]
proporcja=[]
for i in range(0,25):
    proporcja.append(wzrosty[i]/wagi[i])

wagi2 = [wagi for _,wagi in sorted(zip(proporcja,wagi))]
wzrosty2 = [wzrosty for _,wzrosty in sorted(zip(proporcja,wzrosty))]

wagi2.reverse()
wzrosty2.reverse()
print(proporcja)
print(wagi2)
print(wzrosty2)
print('Do windy zmiesci sie osoba o: ')
for k in range(0,25):
    if wagi2[k]<wagawindy:
        wagawindy -= wagi2[k]
        print(' wadze '+str(wagi2[k])+" i wzroscie "+str(wzrosty2[k]))
        waga=waga+wagi2[k]
        wzrost=wzrost + wzrosty2[k]
print(waga)
print(wzrost)