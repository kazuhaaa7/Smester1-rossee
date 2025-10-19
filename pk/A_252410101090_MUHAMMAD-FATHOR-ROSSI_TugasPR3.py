# no 1
# # PROGRAM ONLINE SHOP KHOLIF


produk = { 
    "Iphone 20": 20000, 
    "Macbook Air M4": 40000, 
    "Sosis Kanzler": 35000 
}

print("=== Selamat Datang di Kholis Shop ===")
for nama, harga in produk.items():
    print(f"- {nama}: Rp{harga:,}")

keranjang = [] 
subtotal = 0
ongir = 10000

while True:
    inptprodyk = input("masukkan nama barang yg kamu ingin beli: ").title()

    # validasi barang
    while inptprodyk not in produk:
        inptprodyk = input("Barang yg kamu inginkan tidak tersedia. Pilih barang yg tersedia: ").title()

    jumlahp = int(input("Masukkan jumlah yg anda inginkan: "))
    hargap = produk[inptprodyk]
    total = hargap * jumlahp
    subtotal += total
    keranjang.append((inptprodyk, jumlahp, total))

    choiceagain = input("Apa ada barang yg ingin dibeli lagi? [y/t]: ").lower()
    if choiceagain != "y":
        break

# hitung total
ppn = int(subtotal * 0.12)
totalakhir = subtotal + ppn + ongir

# tampilkan struk
print("\n", "=" * 6, "TRUK PEMBELIAN", "=" * 6)
for nama, jml, tot in keranjang:
    print(f"{nama} x{jml}: Rp{tot}")

print(f"""
--------------------------
Subtotal       : Rp{subtotal}
PPN (12%)      : Rp{ppn}
Ongkir         : Rp{ongir}
--------------------------
Total Akhir    : Rp{totalakhir}

Terima kasih telah berbelanja di toko Kholish!
""")

#no 2
# aku kira nanti bakal  menghitung sesuai keinginan user, jadi nanti user input hingga beberaoa hari ke depan lalu user input kembali "mau liha nominal saldo tabungan di day nabung ke ..." jadi gitu.

daftar = int(input("Masukkan nominal yg akan ditabung: "))

nominal = []
sumnom = 0
nominal.append(daftar)

sumnom += daftar


while True:
    ask = input("Apakah kamu ingin nabung lagi? [Y]/[T]").upper()
    if ask == "Y":
        daftar = int(input("Masukkan lagi nominal yg akan ditabung: "))
    else:
        print("program akan berhenti dan mentotal tabungan kamu")
        break
    sumnom += daftar
    nominal.append(sumnom)

print(sumnom)

# no 3
manystudent = int(input("Masukkan jumlah murid yg ingin diolah datanya: "))
x = 0
nama = []
finalrata = []
while x < manystudent:
    name = input("Masukkan nama yg ingin diolah datanya: ")
    mtk = int(input("Masukkan niai MTK: "))
    fisika = int(input("Masukkan niai FISIKA: "))
    kimia = int(input("Masukkan niai KIMIA: "))
    bio = int(input("Masukkan niai BIOLOGI: "))
    x +=1 
    rata = float((mtk + kimia+ fisika + bio) / 4)
    nama.append(name)
    finalrata.append(rata)
    
print("=" * 8, "HASIL RATA-RATA NILAI", "=" * 8) 
for i in range( 1,manystudent + 1):
    print(f"""
Masukkan data ke-{i}
Nama: {nama[i - 1]}
Mapel MTK: {mtk}
Mapel FISIKA: {fisika}
Mapel KIMIA: {kimia}
Mapel BIOLOGI: {bio}
Rata: {finalrata[i - 1]}
\n
""")