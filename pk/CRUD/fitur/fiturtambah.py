import pandas as pd
import time

def tambah_member():
    nama = input("Masukkan Nama: ").upper()
    try:
        nim = int(input("Masukkan nim:  "))

    except ValueError:
        print("Sedang di proses ya...")
        time.sleep(3)
        print("Masukkan NIM dnegan angka ya :<")
        return
    prodi = input("Masukkan Program Studi: ").upper()

    
    df = pd.read_csv('daftar_mahasiswa.csv') # klo udah dibaca harus disimpa ke csv lagi
    df = pd.concat([df, pd.DataFrame([{'Nama' : nama, 'NIM': nim, 'Prodi': prodi}])], ignore_index=True)
    # why harus dibungkus dgn dict in list: fungsi list, untuk menambahkan bebrapa data/ dict di kasus ini. fungsi dict di sini untuk memanggil dan mengisi value baru di bagian key dict.
    # "Ambil tabel lama, tambahkan 1 baris baru, rapikan index-nya, lalu simpan kembali sebagai df."
    # ignore_index=True dipakai supaya index DataFrame disusun ulang (reset) ketika kamu menggabungkan data baru. melanjutan indx yg udah ada

    df.to_csv('daftar_mahasiswa.csv', index=False)
    print("Data berhasil ditambahkan")