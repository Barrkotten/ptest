#programmet avgör om ett brevs mått upfyller kraven
print ('Skriv in måtten på brevet i mm')
längd = float(input('Längd: '))
bredd = float(input('Bredd: '))
tjocklek = float(input('Tjocklek: '))
summa = float(längd+bredd+tjocklek)
if längd <= 600 and tjocklek <= 100 and summa <= 900 and \
   längd >= 140 and bredd >= 90:
    print('Måtten på brevet är tillåtna')
else:
    print('Måtten på brevet är inte tilåttna')