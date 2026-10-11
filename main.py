import logic
import view

def euclid_biasa(a, b):
    euc = logic.Euclid(a, b)
    euc.euclid()
    view.result_euclid(euc)

def euclid_diperluas(a ,b):
    tes = logic.EuclidDiperluas(a, b)
    tes.euclid_diperluas()
    view.result_euclid_diperluas(tes)

def modular_invers(a, b):
    mod = logic.ModularInvers(a, b)
    mod.modular_invers()
    view.result_invers_modular(mod)

def main():
    while True:
        print(50*"=")
        print("Selamat Datang Di Program Modulus Cryptography")
        print(50*"=")
        print("1. Hitung Euclid")
        print("2. Hitung Euclid Diperluas")
        print("3. Hitung Invers Modular")
        field = int(input("Masukan Opsi Pilihan: "))
        if field == 1:
            a = int(input("Masukan nilai a: "))
            b = int(input("Masukan nilai b: "))
            return euclid_biasa(a, b)
        elif field == 2:
            a = int(input("Masukan nilai a: "))
            b = int(input("Masukan nilai b: "))
            return euclid_diperluas(a, b)
        elif field == 3:
            a = int(input("Masukan nilai a^-1: "))
            b = int(input("Masukan nilai b (mod): "))
            return modular_invers(b, a)
        else:
            ask = input("Apakah anda ingin kembali kemenu? (y/n)")
            if ask == "y" or ask == "Y":
                continue
            else:
                print("Terima Kasih Telah Membantu Menguji Coba..")
                break

main()