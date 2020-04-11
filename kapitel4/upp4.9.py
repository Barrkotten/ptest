#Programmet kommer att skriva ut n antal + tecken. För varje rad kommer antalen + tecken minska med 1 tills det bara blir ett + tecken kvar
n = int(input("Antal rader? "))
for i in range(n, 0, -1):
    for j in range(1, i+1):
        print('+', end='')
    print()
