#input1
nm = input('Nama anda ')
no = input('Nomor Hp anda ')
food = input('makanan atau minuman ')

#rumus1
if food == ('makanan') :
    out = ('nasi goreng , mie goreng , ayam geprek')

elif food == ('minuman'):
    out = ('aneka jus , soft drink , sweet ice tea')

else :
    out = 'ulang'

#outpu1
print(out)

#input2
ps = input ('Pesanan anda ')

#data
if (ps == 'nasi goreng') :
    hg = 15000
elif (ps == 'mie goreng') :
    hg = 12000
elif (ps == 'ayam geprek') :
    hg = 18000
elif (ps == 'aneka jus') :
    hg = 15000
elif (ps == 'soft drink') :
    hg = 10000
elif (ps == 'sweet ice tea') :
    hg = 5000 

#output2
pesanan = int(input('masukan jumlah pesanan = '))

#rumus2
total = hg*pesanan

#output3
print('')
print('Pesanan atas nama ',nm)
print('Dengan no HP ',no)
print('Menu yang anda pesan ',ps)
print('Jumlah pesanan anda ',pesanan)
print('Total harga Rp ', total)

