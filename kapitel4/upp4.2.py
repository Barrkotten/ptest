#programmet läser in talet n och räknar ut summan av 1 + 4 + 9 + 16 ....n^2
n = int(input('Skriv in ett tal'))
summa = 0
k = 1
while k < (n):
    k = k + 1
    print((k*k))
    summa = summa + (k*k)
print('Summan är lika med: ', summa)
