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

def main():
    while True:
        print("Selamat Datang Di Program Modolu Cryptography")
        print("1. Hitung Euclid")
        print("2. Hitung Euclid Diperluas")
        field = int(input("Masukan Opsi Pilihan: "))
        if field == 1:
            a = int(input("Masukan nilai a: "))
            b = int(input("Masukan nilai b: "))
            return euclid_biasa(a, b)
        elif field == 2:
            a = int(input("Masukan nilai a: "))
            b = int(input("Masukan nilai b: "))
            return euclid_diperluas(a, b)
        else:
            ask = input("Apakah anda ingin kembali kemenu? (y/n)")
            if ask == "y" or ask == "Y":
                continue
            else:
                print("Terima Kasih Telah Membantu Menguji Coba..")
                break

main()