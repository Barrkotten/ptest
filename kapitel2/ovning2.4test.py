#Programmet konverterar miles/gallon till liter/mil

#Användaren skriver in bensinförbrukningen i miles/gallon
milesGallon = float(input('Skriv in bensinförburkningen i miles/gallon: '))
#konverterar miles/gallon till mil/gallon
mil = float(milesGallon * 0.1609)
#
faktorn = float(1 / mil)
liter = float(faktorn * 3.785)

print (f'Bensinförbrukning i liter/mil är lika med {liter:.3f}')