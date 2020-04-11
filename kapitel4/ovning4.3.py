#Programmet räknar ut hur många dagar det tar tills man tjänat 10 milj kr. Man tjänar  öre första dagen och lönen fördubblas sedan för varje dag som går.
d = 0
n = 0.01
summa = 0
while summa < 10000000:
    d = d +1
    summa = summa + n
    n = n * 2
    
print ('Antal dagar:', d)
