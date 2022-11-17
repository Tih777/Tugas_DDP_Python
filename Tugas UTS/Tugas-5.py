#Input
v1 = int(input('Input angka pertama = '))
v2 = int(input('Input angka kedua = '))

#Penjelasan
Oprator = ('tambah, kurang, kali, bagi, pangkat ')

print(Oprator)

op = input('Input oprator ')

if (op == 'tambah') :
    hasil = v1+v2

elif (op == 'kurang') :
    hasil = v1-v2

elif (op == 'kali') :
    hasil = v1*v2

elif (op == 'bagi') :
    hasil = v1/v2

elif (op == 'pangkat') :
    hasil = v1**v2

print('Hasilnya adalah ',hasil)