import logic
import os

def result_euclid(euc: logic.Euclid):
    langkah_r = euc.res_r
    langkah_a = euc.temp_a
    langkah_b = euc.temp_b
    judul_a = "LANGKAH A"
    judul_b = "LANGKAH B"
    sisa = "SISA BAGI"
    langkah_iterasi = "INDEX"
    nama_operasi = "EUCLID"
    os.system("cls")
    print(f"{nama_operasi:^50}")
    print(50*"-")
    print(f"{langkah_iterasi:^10} | {judul_a:<10} | {judul_b:<10} | {sisa:<10}")
    print(50*"-")
    for i in range(len(langkah_r)):
        print(f"{i+1:^10} | {langkah_a[i]:^10} | {langkah_b[i]:^10} | {langkah_r[i]:^10}")
    print(50*"-")
    print(f"Hasil Euclid: {euc.hasil}")


def result_euclid_diperluas(euc: logic.EuclidDiperluas):
    langkah_r = euc.res_r
    langkah_q = euc.res_q
    langkah_s = euc.res_s
    langkah_t = euc.res_t
    judul_r = "LANGKAH R"
    judul_q = "LANGKAH Q"
    judul_s = "LANGKAH S"
    judul_t = "LANGKAH T"
    judul_iterasi = "INDEX"
    nama_operasi = "EUCLID DIPERLUAS"
    os.system("cls")
    print(f"{nama_operasi:^65}")
    print(70*"-")
    print(f"{judul_iterasi:^10} | {judul_r:^10} | {judul_q:^10} | {judul_s:^10} | {judul_t:^10}")
    print(70*"-")
    for i in range(len(langkah_r)):
        print(f"{i+1:^10} | {langkah_r[i]:<10} | {langkah_q[i]:<10} | {langkah_s[i]:<10} | {langkah_t[i]:<10}")
    print(70*"-")
    print(f"Hasil Euclid Diperluas: {euc.hasil}")