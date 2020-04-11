#Programmet räknar ut hur många ggr en boll studsar förutsat att den efter varje stud förlorar 30% av sin höjd
höjd = float(input('Skriv in höjden bollen släpptes från i meter: '))
stilla = 0.01
studs = 0
while höjd > stilla:
    höjd = höjd * 0.3
    studs = studs + 1
print ('Antal studs: ',studs)

