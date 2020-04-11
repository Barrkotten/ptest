#Programmet kollar om det första och sista teknet i en text är samma
t = str(input('Skriv valfri text: '))
f = t[0]
s = t[-1]
if f == s:
    print('Det första och sista tecknet är samma')
else:
    print('Det första och sista teknet är inte samma')

    