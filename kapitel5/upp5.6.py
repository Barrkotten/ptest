# Översätter ett svenskt datum till amerikanskt form
s = input('Skriv ett svenskt datum som åååå-mm-dd')
år = s[:4]
månad = s[5:7]
dag = s[8:]
a = månad + '/' + dag + '/' + år[2:]
print('Datumet i amerikansk form', a)

