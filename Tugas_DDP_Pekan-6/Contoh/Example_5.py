a = input("Masukan nama anda ")
b = input("Masukan kelas anda ")
c = int(input("MAsukan nilai anda "))

if  100>c>80:
    ket = "Anda lulus"

elif c>100:
    ket = "Error"

else :
    ket = "Tidak lulus"

print()
print()
print("Nama anda ",a)
print("Kelas anda ",b)
print("Nilai anda ",c)
print("Hasilnya anda dinyatakan ",ket)