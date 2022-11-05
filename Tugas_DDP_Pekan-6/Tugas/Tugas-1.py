# buat program menggunakan logika if untuk 
#permainan roler coster. dengan tinggi minimal 90 
#cm boleh bermain di bawah itu tidak boleh bermain 
#input {nama, umur, tinggi} 
#output {nama , umur, tinggi dan ket} 

#Input
n = input("Masukan nama anda ")
u = input("Masukan umur anda ")
t = int(input("Tingga badan anda "))

#Rumus
if t>90:
    ket = "Boleh bermain"

else :
    ket = "Tidak boleh bermain"

#output
print()
print()
print("Nama anda ",n)
print("Umur anda ",u)
print("Dengan tinggi ",t)
print("Anda ",ket)