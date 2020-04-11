#Programmet ska skriva ut en tabell med värden av funktionen 2x^2-5x+1 när x är -10 - 10
import math
r = 0
for n in range(-10, 11, 1):
    r = r + 1
    värde = (2*math.pow(n,2)-5*n+1)
    print(f'{r:3}{värde:6.0f}')

