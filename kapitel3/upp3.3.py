#Programmet läser in vilket hur många poäng eleven fick på provet och skriver sedan ut betyget
poäng = int(input('Hur många poäng fick du på provet?'))
if poäng < 25:
    print('Du fick tyvärr betyget F')
elif poäng >= 25 and poäng < 30:
     print('Du fick betyget E')
elif poäng >= 30 and poäng < 35:
     print('Du fick betyget D')
elif poäng >= 35 and poäng < 40:
     print('Du fick betyget C')
elif poäng >= 40 and poäng < 45:
     print('Du fick betyget B')
else:
   print('Du fick betyget A')  
