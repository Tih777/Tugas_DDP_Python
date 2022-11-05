#buat program menggunakan logika if untuk 
#praktikum : 
#jika lab tersedia maka praktikum 
#jika lab penuh maka pindah jadwal 
#jika tidak ada lab maka tidak jadi praktikum

#Input
l = input("ketersedian lab : ")

#Rumus
if (l == "tersedia"):
    ket = "praktikum"

elif (l == "penuh"):
    ket = "pindah jadwal"

else :
    ket = "tidak jadi praktikum"

#output
print("Jika lab ",l,"maka",ket)