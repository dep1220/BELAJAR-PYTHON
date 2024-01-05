import os
os.system("cls")

# print Statement
print("Hello Dunia")

# Variabel dan Tipe Data dasar
angka = 10  # -> Tipe data int
desimal = 6.4 # -> Tipe data float
huruf = "Nama" # -> Tipe data str
boolean = True # -> Tipedata bool

# Percabangan dengan if-else
if 20 > 10:
    print("Benar")
else:
    print("Salah")

# Perulangan For
for bilangan_bulat in range(10):
    print(bilangan_bulat, end=" ")

print()

# Perulangan While
nilai = 10
while nilai < 20:
    print(nilai, end=" ")
    nilai += 1

print()

# Fungsi
def pertambahan(angka1,angka2):
    hasil = angka1 + angka2
    return hasil
print(pertambahan(10,20))

# List
kumpulan_data1 = [0, 3, 6, 9, 9.6, True, "Nama"]
print(kumpulan_data1)

# Tuple
# tuple adalah kumpulan data yang tidak bisa di ubah
kumpulan_data2 = (1, 3, 4, 6, 9, True, "Nanas")
print(kumpulan_data2)

# Dictionary
kumpulan_data3 = {
    1 : "mangga",
    2 : "pisang",
    3 : "anggur"
}
print(kumpulan_data3)

# Ini adalah komentar 1 bari yang tidak akan di eksekusi, dan tidak akan membuat program error
"""
Ini adalah komentar untuk lebih dari 1 bari
seperti ini
ini dan 
iniiiii
"""

# Indentasi
user_input = input("Masukkan nama: ")
if user_input != None:
    print("Nama :", user_input) # ini adalah indentasi