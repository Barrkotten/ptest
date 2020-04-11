#Programmet räknar om Fahrenheit till Celsius

fahrenheit = float(input('Ange grader i Fahrenheit'))
celsius = (fahrenheit - 32) * (5/9)
print(f'Antal grader i celsius: {celsius:.1f}C')