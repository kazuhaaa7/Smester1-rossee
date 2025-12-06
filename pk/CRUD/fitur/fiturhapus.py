from tabulate import tabulate
import pandas as pd
import os
import time



def del_member():# error, masih blm spesfik
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

# ================================KASUS APABILA ADA KESALAHAN nan dan Unnamed
# Hapus kolom unnamed jika ada
    # df = df.loc[:, ~df.columns.str.contains("^Unnamed")]
    
    # menghapus value yg bernilai nan. mengahapus 1 kolom apabila axis= menghapus 1, 1 baris apabila axis=0
    df = df.dropna(axis=1)
    
# ============================================================================
# Reset index dan bangun NO dari awal
    df = df.reset_index(drop=True)


# Buang kolom NO lama (kalau ada)
    if 'No' in df.columns:
        df = df.drop(columns=['No'])


#  Buat nomor urut dari index
    df.insert(0, 'No', range(1, len(df)+1)) # untuk rangenya disarankan begitu untuk case tabel
    
    # tampilkan tabel
    print("="* 6, "WELLOME DI PROGRAM HAPUS DATA", "=" * 6)
    print("=" * 6 , "DATA MAHASISWA", "=" * 6)
    headers = ['No','Nama', 'NIM', 'Prodi']
    print(tabulate(df, headers=headers, tablefmt="fancy_grid", showindex=False))


    try:
        idx = int(input("Masukkan index ke berapa yang ingin dihapus: ")) -1 # untuk menyesuaikan dgn index
    # antisipasi jikalau:
        if idx < 0  or idx >= len(df):
            print("Wait yaa...")
            time.sleep(3)
            print('index tdk valid')
            return
        df = df.drop(idx)

    except:
        time.sleep(1)
        print("Masukkan angka ya...")
        print("Tidak berhasil mengahpus data")
        return
    
        
# save action ke csv
    df.to_csv('daftar_mahasiswa.csv', index=False)
    print("Data berhasil dihapus")