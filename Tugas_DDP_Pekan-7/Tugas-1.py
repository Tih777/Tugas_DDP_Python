#input
tr = input (' kendaraan(mobil atau motor) ')
bn = input ('Bensin yang digunakan(pertalite/pertamax/turbo) ')
tj = input ('Tujuan(jakarta/bekasi/depok/tanggerang/bogor) ')

#data bensin

if bn == 'pertalite' :
    harga = 10000
    jarak = 12
elif bn == 'pertamax' :
    harga = 14000
    jarak = 13
elif bn== 'pertamax turbo' :
    harga = 17000
    jarak = 13.5

#data jarak

if tj == 'jakarta' :
    j = 20

elif tj == 'bekasi' :
    j=35.7

elif tj == 'depok' :
    j=5

elif tj == 'tanggerang':
    j=99

elif tj == 'bogor':
    j=120.6

#rumus
tb = j/jarak
hb = (harga/jarak)*j

#output
print("")
print('Kendaraan yang anda pakai ',tr)
print('Bensin yang digunakan ', bn)
print('Tujuan anda ',tj)
print('Total bensin ',tb)
print('Harga bensin Rp',hb)