print ('Välkommen till momsmaskinen')
pris = input('Skriv in varans pris: ')
momssatsen = input('Skriv in varans moms i procent: ')
x = int(pris)
y = int(momssatsen) / 100
moms = x * y
nettopris = x - moms
print(nettopris)
print(moms)


