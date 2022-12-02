def bio1(nama):
    print('Nama anda : '+ nama )

def bio2(tanggal,bulan,tahun):
    print('Tanggal lahir anda :'+ tanggal + '/' + bulan + '/' + tahun)

    now=2022
    umur = now - int(tahun)
    print('Dengan umur : ' , umur)

def bio4(tb):
    print('Tinggi badan anda : '+tb)

    ideal = 110
    bbi=int(tb)- ideal
    print('Berat badan ideal anda : ',bbi,'kg') 

nama = input('Masukan nama anda ')
tanggal = input('Masukan tanggal lahir anda ')
bulan = input('Masukan bulan lahir anda ')
tahun = input('Masukan tahun lahir anda ')
tb = input('Masukan tinggi badan anda ')


print()
print()
bio1(nama)
bio2(tanggal,bulan,tahun)
bio4(tb)