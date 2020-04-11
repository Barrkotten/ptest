#Programmet ska läsa in flera positiva tal och sedan räknat ut vilket är det största och det minsta
n = int(input('Skriv in så många positiva tal du vill \nAvsluta genom att skriva in ett negativt tal'))
m = n
s = n 
x = 0
while True:
    n = int(input('Skriv in så många positiva tal du vill \nAvsluta genom att skriva in ett negativt tal'))
    if n <= 0:
        break
    if n > s:
        s = n
    elif n < m:
        m = n
    else:
        x = n
print('Störsat talet är', s)
print('Minsta talet är', m)
