#Programmet läser in två sidor från en triangel och vinkeln emellan dem.
#Programmet räknar sedan ut om triangeln är liksidig, likbent eller oliksidig
import math
sidaA = float(input('Skriv in längden på första sidan av triangeln: ')) 
sidaB = float(input('Skriv in längden på andra sidan av triangeln: '))
vinkelnGrader = float(input('Skriv in vinkeln mellan de två sidorna: '))
vinkelnRadianer = math.radians(vinkelnGrader)
sidaC = math.sqrt( math.pow(sidaA, 2) + math.pow(sidaB, 2) - 2 * sidaA * sidaB * math.cos(vinkelnRadianer))
skillnadAB = abs(sidaA - sidaB)
skillnadAC = abs(sidaA - sidaC) 
skillnadBC = abs(sidaB - sidaC) 
if skillnadAB < math.pow(10,-10) and skillnadAC < math.pow(10,-10) and skillnadBC < math.pow(10,-10):
    print('Triangeln är liksidig')
elif skillnadAB < math.pow(10,-10) or skillnadAC < math.pow(10,-10) or skillnadBC < math.pow(10,-10):
    print('Tringeln är likbent')
else: 
    print('Tringeln är oliksidig')
