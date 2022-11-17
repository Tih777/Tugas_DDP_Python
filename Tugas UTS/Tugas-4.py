#Input
d1 = input('Masukan d1= ')
d2 = input('Masukan d2= ')
s1 = int(input('Masukan sisi AB/BC= '))
s2 = int(input('Masukan sisi CD/DA= '))

#Rumus
luas = 0.5*float(d1)*float(d2)
kel1 = 2 * (s1 + s2)

#output
print('Luas dari layang-layang = ',luas)
print('Keliling dari layang-layang = ',kel1)