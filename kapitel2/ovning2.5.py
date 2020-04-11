#Programmet beräknar avståndet mellan två punkter i ett tvådimensionellt koordinatsystem
import math
#Användaren skriver in de två första punkterna
x1, y1= [float(x) for x in input('Ange första punketns koordinater: ').split()]
x2, y2= [float(y) for y in input('Ange andra punketns koordinater: ').split()]
#Beräknar avståndet mellan punkterna med Avståndsformeln
s = float(math.sqrt(math.pow((x1-x2), 2) + math.pow((y1-y2), 2))) 
#Skriver ut resultatet
print(f'Sträckan mellan punkterna är lika med: {s:.1f}')




  