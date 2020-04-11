#programmet räknar ut kostnad för ett abonnemang når man ringer x antal minuter i månaden.
# Om man ringer för mer än 300kr i månaden för man 10% rabbat
min = float(input('Skriv in hur många minuter du ringer varje månad: '))
minKostnad = min * 0.5
if minKostnad > 300:
    minKostnad = minKostnad * 0.9
print(minKostnad)