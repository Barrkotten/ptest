#Programmet konverterar miles/gallon till liter/mil

#Användaren skriver in bensinförbrukningen i miles/gallon
milesGallon = float(input('Skriv in bensinförburkningen i miles/gallon: '))
#konverterar miles/gallon till km/gallon
km = float(milesGallon * 1.609)
#
milfaktorn = float(10 / km)
liter = float(milfaktorn * 3.785)

print (f'Bensinförbrukning i liter/mil är lika med {liter:.3f}')