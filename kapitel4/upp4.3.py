#programmet läser in talet n och beräknar summan av 1/1 + 1/2 + 1/3 ... 1/n
n = int(input('Skriv in ett tal'))
summa = 0
k = 0
while k < n:
    k = k + 1
    print (1/k)
    summa = summa + (1/k)
print(f'Summan är lika med {summa:.3}')