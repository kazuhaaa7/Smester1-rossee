import pandas as pd
import os

# membuat csv langsung di sini
file_name = 'daftar_mahasiswa.csv'

# cek, apakah file csv sudah ada #1
# if not os.path.exists(file_name):
#     # buat file csv kosong dgn header
#     df = pd.DataFrame(columns=['Nama','NIM', 'Prodi'])
#     df.to_csv('daftar_mahasiswa.csv', index=False)
#     print('flle csv sudah dibuat')
# else:
#     print('file sudah ada')

# cek, apakah file csv sudah ada #2
try:
    pd.read_csv('daftar_mahasiswa.csv')
except FileNotFoundError:
    df = pd.DataFrame({'Nama': [], 'NIM': [], 'Prodi': []})
    df.to_csv('data_sederhana.csv', index=False)


def show_data():
    df = pd.read_csv('daftar_mahasiswa.csv')
    print(df)

def tambah_member():
    nama = input("Masukkan Nama: ")
    nim = int(input("Masukkan nim:  "))
    prodi = input("Masukkan Program Studi: ")
    df = pd.read_csv('daftar_mahasiswa.csv') # klo udah dibaca harus disimpa ke csv lagi
    df = pd.concat([df, pd.DataFrame([{'Nama' : nama, 'NIM': nim, 'Prodi': prodi}])], ignore_index=True)
    # whh harus dibungkus dgn dict in list: fungsi list, untuk menambahkan bebrapa data/ dict di kasus ini. fungsi dict di sini untuk memanggil mengisi value baru di bagian key dict.
    # "Ambil tabel lama, tambahkan 1 baris baru, rapikan index-nya, lalu simpan kembali sebagai df."
    df.to_csv('daftar_mahasiswa.csv', index=True)
    print("Data berhasil ditambahkan")

def ubah_member():# masih eror, ini ga spesfik karna pebubahan datanya masih rancu
    show_data()
    nama = input('Masukkana nama yg ingin diubah: ')
    nim_baru = int(input("Masukkan NIM yg baru: "))
    prodi_baru = input('Masukkan Prodi yg ingin kamu ubah: ')
    # baca csv
    df = pd.read_csv('daftar_mahasiswa.csv')
    # eksekusi
    df.loc[df['Nama'] == nama, 'NIM' == nim_baru, 'Prodi' == prodi_baru]
    # add to csv
    df.to_csv('daftar_mahasiswa.csv', index=True)# apabila index=true, maka ada kolom tambahan no index yg sebenernya tdk terlalu dibutuhkan

def del_member():# error, masih blm spesfik
    nama = input('Masukkana nama yg ingin dihapus: ')
    # baca file
    df = pd.read_csv('daftar_mahasiswa.csv')
    df = df[df['Nama'] != nama]
    df.to_csv('data_sederhana.csv', index=True)



while True:
    print("1. Tambah Data")
    print("2. Tampilkan Data")
    print("3. Ubah Data")
    print("4. Hapus Data")
    print("5. Keluar")
    pilihan = input("Pilih menu (1/2/3/4/5): ")
    if pilihan == '1':
        tambah_member()
    elif pilihan == '2':
        show_data()
    elif pilihan == '3':
        ubah_member()
    elif pilihan == '4':
        del_member()
    # elif pilihan == '5':
        # break
    else:
        print("Pilihan tidak valid.")
