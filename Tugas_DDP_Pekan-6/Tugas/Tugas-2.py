#buat program menggunakan logika if untuk 
#menghitung nilai : 
#jika 90 - 100 = "istimewa" 
#jika 70 - 89 = "sangat bagus" 
#jika 60 - 69 = "cukup"
#jika <60 = "gagal" 
#input {nama, kelas, nilai} 
#output {nama , kelas, nilai dan ket} 

#input
na = input("Masukan nama : ")
k = input("Masukan kelas : ")
n = int(input("Masukan nilai anda : "))

#Rumus
if 101>n>89:
    ket = "istimewa"

elif 90>n>69:
    ket = "sangat bagus"

elif 70>n>59:
    ket = "cukup"

elif n<60:
    ket = "gagal"

else :
    ket = "Error"

#output
print()
print()
print("Nama  : ",na)
print("Kelas : ",k)
print("Nilai : ",n)
print("Kamu  : ",ket)