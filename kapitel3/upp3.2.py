kortPris = float(input('Skriv in priset på ett årskort på ditt gym: '))
biljettPris, ggr = [float(x) for x in input('Ange priset för en biljett och antal planerade besök per år').split()]
totalPris = biljettPris * ggr
skillnad = kortPris - totalPris
if skillnad < 0:
    skillnad = skillnad * -1
if kortPris < totalPris:
    print('Köp årskort! Det är', skillnad, 'kr billigare än biljetter')
else:
    print('Köp biljetter! Det är', skillnad, 'kr billigare än årskort')


