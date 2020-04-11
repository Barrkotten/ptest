#programmet läser in talet n och räknar ut summan av 1 + 4 + 9 + 16 ....n^2 (Samma som upp4.2 men med for istället för while-sats)
n = int(input('Skriv in ett tal'))
n =  n + 1
summa = 0
for k in range (1, n, 1):
    print(k*k)
    summa = summa + (k*k)
print('Summan är lika med: ', summa)