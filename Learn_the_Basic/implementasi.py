import os

def kalkulator_sederhana():
    os.system("cls")
    while(True):
        user_option = input("Silahkan Pilih Operasi [+, -, *, /] : ")
        match(user_option):
            case "+":
                angka1 = int(input("Angka pertama: "))
                angka2 = int(input("Angka kedua: "))
                perhitungan = angka1 + angka2
                print(angka1," + ", angka2, " = ", perhitungan)
            case "-":
                angka1 = int(input("Angka pertama: "))
                angka2 = int(input("Angka kedua: "))
                perhitungan = angka1 - angka2
                print(angka1," - ", angka2, " = ", perhitungan)
            case "*":
                angka1 = int(input("Angka pertama: "))
                angka2 = int(input("Angka kedua: "))
                perhitungan = angka1 * angka2
                print(angka1," * ", angka2, " = ", perhitungan)
            case "/":
                angka1 = int(input("Angka pertama: "))
                angka2 = int(input("Angka kedua: "))
                perhitungan = angka1 / angka2
                print(angka1," / ", angka2, " = ", perhitungan)
            case _: print("Operasi tidak valid")
        is_done = input("Apakah Sudah Selesai (y/n)? ")
        if is_done == "y" or is_done == "Y":
            break
        print("-"*50)


def menghitung_gajih_bersih():
    """Fungsi menghitung gajih bersih setelah dipotong pajak 5%"""
    while(True):
        os.system("cls")
        nama = input("Nama\t\t: ")
        tunjangan = int(input("Tunjangan\t: "))
        gajih_pokok = int(input("Gajih Pokok\t: "))

        pajak = (5*(tunjangan + gajih_pokok))/100
        gajih_bersih = (tunjangan + gajih_pokok) - pajak

        os.system("cls")
        print("="*30)
        print(" "*8+"GAJIH BERSIH")
        print("="*30)
        print(f"Nama\t\t : {nama}")
        print(f"Tunjangan\t : {tunjangan}")
        print(f"Pajak\t\t : {pajak}")
        print(f"Gajih Pokok\t : {gajih_pokok}")
        print(f"Gajih Bersih\t : {gajih_bersih}")

        is_done = input("Apakah sudah selesai (y/n)? ")
        if is_done == "y" or is_done == "Y":
            break

def menghitung_rata_nilai():
    while(True):
        os.system("cls")
        jumlah_nilai = int(input("Masukan jumlah nilai yang akan di hitung : "))
        total_nilai = 0
        for x in range(jumlah_nilai):
            kumpulan_nilai = int(input("Nilai ke-"+str(x+1) + ": "))
            total_nilai += kumpulan_nilai
        rata_rata_nilai = total_nilai / jumlah_nilai
        print("Rata - rata nilai yaitu : ",round(rata_rata_nilai,2))
        is_done = input("Apakah sudah selesai (y/n)? ")
        if is_done == 'y' or is_done == 'Y':
            break


def konversi_suhu_celsius():
    while(True):
        os.system("cls")
        print("="*40)
        print(" "*10+"MENU-MENU KONVERSI")
        print("="*40)
        print("[1] Celsius -> Fahrenheit")
        print("[2] Celsius -> Kelvin")
        print("[3] Celsius -> Reamur")
        print("-"*40)
        user_option = input("Pilih menu konversi [1,2,3] ")
        match(user_option):
            case "1":
                celsius_input = float(input("Masukkan Suhu Celsius: "))
                fahrenheit = (9/5) * celsius_input + 32
                print(f"{celsius_input} pada celsius sama dengan {round(fahrenheit,2)} pada fahrenheit")
            case "2":
                celsius_input = float(input("Masukkan Suhu Celsius: "))
                kelvin = celsius_input + 273.15
                print(f"{celsius_input} pada celsius sama dengan {round(kelvin,2)} pada kelvin")
            case "3":
                celsius_input = float(input("Masukkan Suhu Celsius: "))
                reamur = (4/5) * celsius_input
                print(f"{celsius_input} pada celsius sama dengan {round(reamur,2)} pada reamur")
            case _: print("Pilihan tidah valid")
        is_done = input("Apakah sudah selesai(y/n)? ")
        if is_done == "y" or is_done == "Y":
            break

class objek_catatan:
    def __init__(self):
        self.catatan = {}
    
    def tambah_catatan(self, judul, isi):
        self.catatan[judul] = isi
        print(f"Catatan '{judul}' telah ditambahkan")
    
    def lihat_catatan(self):
        if(self.catatan):
            print("-"*40)
            print(" "*13+"Daftar catatan")
            print("-"*40)
            for judul, isi in self.catatan.items():
                print(f"Judul : {judul}\nIsi: {isi} \n{'-'*40}")
        else:
            print("Tidak ada catatan, tekan enter aja cuyy")

    def edit_catatan(self, judul, isi_baru):
        if judul in self.catatan:
            self.catatan[judul] = isi_baru
            print(f"Catatan '{judul}' telah diubah")
        else:
            print(f"Catan dengan {judul} tidak di temukan")

    def hapus_catatan(self, judul):
        if judul in self.catatan:
            del self.catatan[judul]
            print("Catatan berhasil dihapus")
        else:
            print("Catatan dengan {judul} tidak di temukan")
        

def aplikasi_catatan_sederhana():
    aplikasi = objek_catatan()
    while(True):
        os.system("cls")
        print("="*40)
        print(" "*10+"MENU APLIKASI CATATAN")
        print("="*40)
        print("[1] Tambah Catatan")
        print("[2] Tampilkan Catatan")
        print("[3] Edit Catatan")
        print("[4] Hapus Catatan")
        print("[0] Keluar")
        print("-"*40)
        user_option = input("Silahkan Pilih Menu [1,2,3,4,0]: ")
        match user_option:
            case "1":
                judul = input("Judul catatan : ")
                isi_catatan = input("Isi catatan : ")
                aplikasi.tambah_catatan(judul, isi_catatan)
                input()
            case "2":
                aplikasi.lihat_catatan()
                input()
            case "3":
                aplikasi.lihat_catatan()
                judul = input("Masukan judul catatan yang akan di ubah : ")
                isi_baru = input("Masukan isi catatan baru : ")
                aplikasi.edit_catatan(judul, isi_baru)
                input()
            case "4":
                aplikasi.lihat_catatan()
                judul = input("Masukan judul catatan yang akan dihapus : ")
                aplikasi.hapus_catatan(judul)
                input()
            case "0": break
            case _ : print("Pilihan yang anda masukan invalid")

while(True):
    os.system("cls")
    print("="*50)
    print("PROGRAM SEDERHANA DARI BELAJAR DASAR PYTHON")
    print("="*50)
    print(17*" " + "MENU APLIKASI")
    print("-"*50)
    print("[1] Kalkulator Sederhana")
    print("[2] Menghitung Gajih Bersih")
    print("[3] Menghitung Rata-rata nilai")
    print("[4] Confersi_satuan_suhu")
    print("[5] Aplikasi Catatan Sederhana")
    print("[0] KELUAR")
    print("-"*50)

    user_option = input("Pilih Aplikasi [1,2,3,4,5,0] : ")

    match(user_option):
        case "1": kalkulator_sederhana()
        case "2": menghitung_gajih_bersih()
        case "3": menghitung_rata_nilai()
        case "4": konversi_suhu_celsius()
        case "5": aplikasi_catatan_sederhana()
        case "0":
            print("\nTERIMAKASIH TELAH MENGGUNAKAN APLIKASI KAMI\n")
            break
        case _: print("Pilihan Tidah Valid")