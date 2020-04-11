#Programmet ska hitta det först vita teknet med hjälp av en for-sats
s = input('Skriv en text ')
i = 0
for a in range(0,len(s)+1,1):
    c = s[a]
    if c == ' ' or c == '\t':
        break
    i = i + 1
if i < len(s):
    print(f'Det första vita tecknet finns på plats {i}')
else:
    print("Det finns inga vita tecken")