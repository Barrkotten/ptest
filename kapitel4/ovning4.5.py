#Programmet ska räkna ut antal invånare i en kommun efter x antal år med hjälp av vissa vilkor.
antal_inv = 26000
flytt = 25
n = 0
tid = int(input('Skriv hur många år fram i tiden du vill veta antalet invånare'))
while n < tid:
    mortalitet = 0.006 * antal_inv
    nativitet = 0.007 * antal_inv
    antal_inv = antal_inv - mortalitet + nativitet - flytt
    n = n + 1
år = 2019 + tid
print(f'Antal invånare år {år}: {antal_inv:.0f}')

