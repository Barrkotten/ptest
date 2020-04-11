#Programmet ska skriva ut en tabell bestående av talen 1-12 och talen i både kvadrat och kubik
import math
n = 1
while n < 13:
    kv = math.pow(n, 2)
    ku = math.pow(n, 3)
    print(f'{n:.0f}{kv:6.0f}{ku:6.0f}')
    n = n+1