#Programmet tar reda på vilken position det sista "vita tecknet" har
s = input('Skriv en text ')
#Skriver om texten baklänges
a = s[::-1]
i = 0
for c in a:
    if c == ' ' or c == '\t':
        break
    i = i + 1
if i < len(s):
    #Extra "-1" för att len(s) börjar inte räkna på 0. 
    i = len(s) - i - 1
    print(f'Sista vita tecknet finns på plats: {i} ')
else:
    print('Det finns inget vit tecken')