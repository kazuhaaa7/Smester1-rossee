from fitur import fiturtambah as tambah
from fitur import fiturubah as ubah
from fitur import fiturhapus as hapus
from tabulate import tabulate
import pandas as pd
import os

# membuat csv langsung di sini
file_name = 'daftar_mahasiswa.csv'

# cek, apakah file csv sudah ada #1 - use if-else
# if not os.path.exists(file_name):
#     # buat file csv kosong dgn header
#     df = pd.DataFrame(columns=['Nama','NIM', 'Prodi'])
#     df.to_csv('daftar_mahasiswa.csv', index=False)
#     print('flle csv sudah dibuat')
# else:
#     print('file sudah ada')

# cek, apakah file csv sudah ada #2 - use try-except
try:
    pd.read_csv('daftar_mahasiswa.csv')
except FileNotFoundError:
    df = pd.DataFrame({'Nama': [], 'NIM': [], 'Prodi': []})
    df.to_csv('daftar_mahasiswa.csv', index=False)


def show_data():
    df = pd.read_csv('daftar_mahasiswa.csv')

# Hapus kolom unnamed jika ada
# df = df.loc[:, ~df.columns.str.contains("^Unnamed")] #cari aa maksudnya

# untuk menghapus value nan
    df = df.dropna(axis=1)
    

# =================================================================== tabel
    # data show only
        # Buang kolom NO lama kalau ada
    if 'No' in df.columns:
        df = df.drop(columns=['No'])

    #  Buat nomor urut dari index
    df.insert(0, 'No', range(1, len(df)+1)) # untuk rangenya disarankan begitu untuk case tabel
    # arti dri kode di atas(df.insert): (mau di taro dii indx kolom brp, <nama kolom>, <akan muncul brp banyak>)

    print("=" * 6 , "DATA MAHASISWA", "=" * 6)
    headers = ['No','Nama', 'NIM', 'Prodi']
    print(tabulate(df, headers=headers, tablefmt="fancy_grid", showindex=False))
# ===================================================================

while True:
    print("1. Tampilkan Data")
    print("2. Tambah Data")
    print("3. Ubah Data")
    print("4. Hapus Data")
    print("5. Keluar")
    pilihan = input("Pilih menu (1/2/3/4/5): ")
    if pilihan == '1':
        show_data()
    elif pilihan == '2':
        tambah.tambah_member()
    elif pilihan == '3':
        ubah.ubah_member()
    elif pilihan == '4':
        hapus.del_member()
    elif pilihan == '5':
        break
    else:
        print("Pilihan tidak valid.")
        exit()
