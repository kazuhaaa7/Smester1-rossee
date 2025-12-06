from tabulate import tabulate
import pandas as pd
import time
import os




def ubah_member():# masih eror, ini ga spesfik karna pebubahan datanya masih rancu
    os.system('cls')
    print("""

██╗░░██╗░█████╗░███████╗██╗░░░██╗██╗░░██╗░█████╗░░█████╗░░█████╗░██╗░██████╗
██║░██╔╝██╔══██╗╚════██║██║░░░██║██║░░██║██╔══██╗██╔══██╗██╔══██╗╚█║██╔════╝
█████═╝░███████║░░███╔═╝██║░░░██║███████║███████║███████║███████║░╚╝╚█████╗░
██╔═██╗░██╔══██║██╔══╝░░██║░░░██║██╔══██║██╔══██║██╔══██║██╔══██║░░░░╚═══██╗
██║░╚██╗██║░░██║███████╗╚██████╔╝██║░░██║██║░░██║██║░░██║██║░░██║░░░██████╔╝
╚═╝░░╚═╝╚═╝░░╚═╝╚══════╝░╚═════╝░╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚═╝░░░╚═════╝░
""")
    df = pd.read_csv('daftar_mahasiswa.csv')

    # Hapus kolom unnamed jika ada
    df = df.loc[:, ~df.columns.str.contains("^Unnamed")]
# df.columns	Ambil semua nama kolom
# .str.contains("^Unnamed")	Cek kolom mana yang namanya diawali "Unnamed"
# ~	Negasi (kebalikan) → pilih kolom yang bukan Unnamed
# df.loc[:, ...]	Pilih semua baris (:) dan hanya kolom yang cocok dengan filter
# Jadi hasilnya hanya kolom valid, tanpa kolom “Unnamed…”.


# .loc untuk	Nama kolom/baris	df.loc[:, ['Nama','NIM']]
# .iloc  untuk	Index angka	df.iloc[:, [0,1]]

    # Reset index biar rapi lagi
    df = df.reset_index(drop=True )
        
    # Buang kolom NO lama kalau ada
    if 'No' in df.columns:
        df = df.drop(columns=['No'])


    #  Buat nomor urut dari index
    # format .insert by pandas: DataFrame.insert(loc, column, value, allow_duplicates=False)
    df.insert(0, 'No', range(1, len(df)+1)) # untuk rangenya disarankan begitu untuk case tabel

    # tampilkan data dulu
    print("="* 6, "WELLOME DI PROGRAM UBAH DATA", "=" * 6)

    print("=" * 6 , "DATA MAHASISWA", "=" * 6)
    headers = ['No','Nama', 'NIM', 'Prodi']
    print(tabulate(df, headers=headers, tablefmt="fancy_grid", showindex=False))

# error handling
    try:
        idx = int(input("Masukkan value indeks kek berapa yang akan diubah: ")) -1
        if idx < 0  or idx >= len(df):
            print('index tidak valid')
            return
        
    except:
        print("input harus angka")
        return


    nama_baru = input('Masukkan nama yang baru: ').upper()
    try:
        nim_baru = int(input("Masukkan NIM yang baru: "))
    except ValueError:
        print("Sedang di proses ya...")
        time.sleep(3)
        print("Masukkan NIM dnegan angka ya :<")
        return
    prodi_baru = input('Masukkan Prodi yang baru: ').upper()


    # eksekusi, harus satu satu ya. ga bisa bebarengan
    df.loc[idx,'Nama'] = nama_baru
    df.loc[idx,'NIM'] = nim_baru
    df.loc[idx,'Prodi'] = prodi_baru


    # add to csv|  # harus save ya stelah mmebaca csv
    df.to_csv('daftar_mahasiswa.csv', index=False)# apabila index=true, maka ada kolom tambahan no index yg sebenernya tdk terlalu dibutuhkan
    print("Data berhasil Diubah")
