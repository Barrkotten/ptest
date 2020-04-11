#Programmet läser in x antal rader och skriver sedan ut x antal rader av multiplikationstabellen
l = int(input('Skriv in antal rader'))
v = int(input('Skriv in antal rader'))
for n in range (1, l+1, 1):
    for m in range(n,(n*v)+1, n):
        print(f'{m:3} ', end='')
    print()