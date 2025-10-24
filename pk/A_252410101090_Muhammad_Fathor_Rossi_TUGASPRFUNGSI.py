def menu():
    print("=" * 20)
    print("KALKULATOR")
    print("=" * 20)
    print("""
    1. Tambah (+)
    2. Kurangi (-)
    3. Perkalian (*)
    4. Modulus (%)
    5. Pembagian (/)
    6. Pangkat (^)
    7. Riwayat
    0. Keluar
""")
    while True:
        pil = input("Masukkan menu yg dipilih: ")
    # .split() => untuk menyamarkan spasi apabila ada, type akan berubah menjadi list
        if pil == "1":
            Tambah()
        elif pil == "2":
            Kurangi()
        elif pil == "3":
            Perkalian()
        elif pil == "4":
            Modulus()
        elif pil == "5":
            Pembagian()
        elif pil == "6":
            Pangkat()
        elif pil == "7":
            Riwayat()
        else:
            print("Inputan salah")

    
def Tambah():
    nilai1 = float(input("inputkan nilai 1: ")) # untuk memblok kade supayay ga error
    nilai2 = float(input("inputkan nilai 2: "))
    jumlah = nilai1 + nilai2
    print(f"hasil dari {nilai1} + {nilai2} = {jumlah}") # untuk memblok kade supayay ga error
    Riwaya_t(f"{nilai1} + {nilai2} = {jumlah}")


def Kurangi():
    nilai1 = float(input("inputkan nilai 1: ")) # untuk memblok kade supayay ga error
    nilai2 = float(input("inputkan nilai 2: "))
    jumlah = nilai1 - nilai2
    print(f"hasil dari {nilai1} - {nilai2} = {jumlah}") # untuk memblok kade supayay ga error
    Riwaya_t(f"{nilai1} - {nilai2} = {jumlah}")

def Perkalian():
    nilai1 = float(input("inputkan nilai 1: ")) # untuk memblok kade supayay ga error
    nilai2 = float(input("inputkan nilai 2: "))
    jumlah = nilai1 * nilai2
    print(f"hasil dari {nilai1} x {nilai2} = {jumlah}") # untuk memblok kade supayay ga error
    Riwaya_t(f"{nilai1} * {nilai2} = {jumlah}")

def Pembagian():
    nilai1 = float(input("inputkan nilai 1: ")) # untuk memblok kade supayay ga error
    nilai2 = float(input("inputkan nilai 2: "))
    jumlah = nilai1 / nilai2
    print(f"hasil dari {nilai1} / {nilai2} = {jumlah}") # untuk memblok kade supayay ga error
    Riwaya_t(f"{nilai1} / {nilai2} = {jumlah}")
    
def Modulus():
    nilai1 = float(input("inputkan nilai 1: ")) # untuk memblok kade supayay ga error
    nilai2 = float(input("inputkan nilai 2: "))
    jumlah = nilai1 % nilai2
    print(f"hasil dari {nilai1} % {nilai2} = {jumlah}") # untuk memblok kade supayay ga error
    Riwaya_t(f"{nilai1} % {nilai2} = {jumlah}")

def Pangkat():

    nilai1 = float(input("inputkan nilai 1: ")) # untuk memblok kade supayay ga error
    nilai2 = float(input("inputkan nilai 2: "))
    jumlah = nilai1  ** nilai2
    print(f"hasil dari {nilai1} ^ {nilai2} = {jumlah}") # untuk memblok kade supayay ga error
    Riwaya_t(f"{nilai1} ^ {nilai2} = {jumlah}")


Riwayatakhir = []

def Riwaya_t(nilai):
    Riwayatakhir.append(nilai) # untuk memblok kade supayay ga error

def Riwayat():
    if not Riwayatakhir:
        print("BLM ADA RIWAYAT")
    else:
        print("HASIL DARI OPERASI")
        for i, item in enumerate(Riwayatakhir, start=1): # untuk memblok kade supayay ga error
            print(f"Operasi : {i}, {item}")

menu()