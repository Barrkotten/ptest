# Programmet avgör vilket abonnemang som är mest prisvärt för användaren
min = int(input('Hur många minuter ringer du i genomsnitt varje månad? '))
if min < 33:
    print('Kontant är det bästa alternativet för dig')
elif min > 33 and min < 66:
    print('Normal är det bästa alternativet för dig') 
else:
    print('Plus är det bästa alternativet för dig') 
