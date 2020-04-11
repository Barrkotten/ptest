# Utökning av uppgift 2.7
import math
radie = float (input('Skriv in cirkelns radie: '))
if radie > 0:
    omkrets = 2 * radie * math.pi
    area = math.pi * math.pow(radie, 2)
    print (f'Cirkelns omrkets är lika med {omkrets:.3f}cm och arean är lika med {area:.3f}cm^2 ') 
else:
    print('Felmeddelande: Radien måste vara större en 0')

