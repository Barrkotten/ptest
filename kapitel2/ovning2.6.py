#Programmet räknat ut hur många procent av isotopen C^14 som är kvar efter S antal år.
#Halveringstiden på C^14 är 5730år
#Programmet använder formerln n=n0e^-{λ*t}
#λ räknas ut med formeln λ = ln2/T
import math
s = float(input('Skriv in antal år:'))

#Raderna 9-12 är samma som rad 14 fast uppdelat i flera segment
#lambda_ = (math.log(2)/5730)
#lambda_tid = lambda_ * s
#n = math.exp(lambda_tid)
#nProcent = 1 / n * 100
s = int(s)
nProcent = float(1 / (math.exp((math.log(2)/5730)* s)) * 100) 
print(f'Antal procent av änmet kvar efter {s} år är lika med {nProcent:.2f}%') 
