#Programmet räknar ut volymen och arean på en sfär

import math
radie = float(input('Skriv sfärens radie: '))
volym = float(4 * math.pi * math.pow(radie, 3) / 3)
area = float(4 * math.pi * math.pow(radie, 2))
print(f'Volymen är lika med {volym:.2f}cm^3 och arean är lika med {area:.2f}cm^2')
