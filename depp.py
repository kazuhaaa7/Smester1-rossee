# terlalau bertele tele, memakai banyak variabel, padahal fungsinya sma cuma penempatanny aja yg berbeda.


# KEMBANGKAN LAGI, IN UDAH TERLALU JAUH DAN INTERAKLTIF
# ===========================
# PROGRAM ONLINE SHOP KHOLIF
# ===========================

# Daftar produk dan harga
produk = {
    "Iphone 20": 20000,
    "Macbook Air M4": 40000,
    "Sosis Kanzler": 35000
}

keranjang = []  # list untuk simpan (produk, jumlah, subtotal)
ongkir = 10000
ppn = 0.12

print("=== Selamat Datang di Kholish Shop ===")
print("Kami menjual:")
for nama, harga in produk.items():
    print(f"- {nama}: Rp{harga:,}")

# -------------------------------
# INPUT JUMLAH PRODUK YANG AKAN DIBELI
# -------------------------------
while True:
    banyak_barang_input = int(input("\nBerapa banyak jenis barang yang ingin kamu beli? "))

    if banyak_barang_input <= 0:
        print("Jumlah barang minimal 1!")
        continue
    break  # keluar kalau input valid

# -------------------------------
# LOOP UNTUK MEMASUKKAN TIAP BARANG
# -------------------------------

for i in range(1, banyak_barang_input + 1):
    print(f"\nBarang ke-{i}:")
    sales = input("Masukkan nama produk: ").title()

    if sales not in produk:
        print("TETOTT... Produk tidak ada di daftar. Coba lagi.")
        continue

    jumlah_input = int(input("Masukkan jumlah produk yang ingin dibeli: "))

    subsubtotal = produk[sales] * jumlah_input
    keranjang.append((sales, jumlah_input, subsubtotal))
    print(f"✅ {sales} sebanyak {jumlah_input} buah berhasil ditambahkan ke keranjang.")

    # LOOP AGAR BISA MENAMBAH LAGI SETELAH UDAHD MENENTUKAN JUMLAH BARANG YG INGIN DIBELI
while True:
    nextStep = input("Apa ada barang yg ingin ditambahkan ke pembelanjaan lagi? [y]/[t]: ").lower()
    if nextStep == "y" or nextStep != "t":
        banyak_barang_input_tambahan = int(input("\nBerapa banyak jenis barang yang ingin kamu beli lagi? "))

        for i in range(1, banyak_barang_input + 1):
            print(f"\nBarang ke-{i}:")
            sales = input("Masukkan nama produk: ").title()

        if sales not in produk:
            print("TETOTT... Produk tidak ada di daftar. Coba lagi.")
            continue
            
        elif banyak_barang_input_tambahan <= 0:
            print("Jumlah barang minimal 1!")
            continue
        break  # keluar kalau input valid
# error
    elif nextStep == "t":
        print("baik program akan kami tutu")
        continue
    # error
    print("-" * 35)
    print(f"Subtotal : Rp{subsum}")
    print(f"PPN (12%): Rp{int(finalpajak):,}")
    print(f"Ongkir   : Rp{ongkir:,}")
    print("-" * 35)
    print(f"Total Bayar: Rp{int(bosssum):,}")
    print("Terima kasih telah berbelanja di toko Kholish! ")

# -------------------------------
# LOOP UNTUK MEMASUKKAN TIAP BARANG LAGEEE
# -------------------------------

for x in range(1, banyak_barang_input_tambahan + 1):
    print(f"\nBarang ke-{i}:")
    nextStep = input("Masukkan nama produk: ").title()


    if nextStep not in produk:
        print("TETOTT... Produk tidak ada di daftar. Coba lagi.")
        continue
    jumlah_input_tambahan = int(input("Masukkan jumlah produk yang ingin dibeli lagi: "))
    subsubtotal_tambahan = produk[sales] * jumlah_input
    keranjang.append((nextStep, jumlah_input_tambahan, subsubtotal_tambahan))
    print(f"✅ {nextStep} sebanyak {jumlah_input_tambahan} buah berhasil ditambahkan ke keranjang.")


# -------------------------------
# CHECKOUT DAN PERHITUNGAN TOTAL
# -------------------------------
if keranjang:
    print("\n" + "=" * 8, "STRUK BELANJA", "=" * 8)
    subtotal = 0

    # for i, (nama_produk, jumlah, subsubtotal) in enumerate(keranjang, start=1):
    #     print(f"{i}. {nama_produk} x {jumlah} = Rp{subsubtotal:,}")
    #     subtotal += subsubtotal
    

    #LOOP AWAL 
    # error
    for i, (nama_produk, jumlah, subsubtotal) in range(1, keranjang + 1):
        print(f"{i}. {nama_produk} x {jumlah} = Rp.{subsubtotal:,}")
        subtotal += subsubtotal
    # LOOP TAMBAHAN
    for x, (nama_produk_tambahan, jumlah_tambahan, sum_tambahan) in range (1, keranjang + 1):
        print(f" {x}. {nama} x {jumlah_tambahan} = Rp.{sum_tambahan}")
        sum += sum_tambahan
 
    # TOTAL HARGA LOOP AWAL
    pajak = subtotal * ppn
    total = subtotal + pajak + ongkir

    #TOTAL HARGA LOOP TAMBAHAN
    pjk = sum * ppn
    finalsum = sum + pjk + ongkir

    # FINALLY
    finalpajak = pjk + pajak
    bosssum = total + finalsum
    subsum = subtotal + sum

    print("-" * 35)
    print(f"Subtotal : Rp{subsum:,}")
    print(f"PPN (12%): Rp{int(finalpajak):,}")
    print(f"Ongkir   : Rp{ongkir:,}")
    print("-" * 35)
    print(f"Total Bayar: Rp{int(bosssum):,}")
    print("Terima kasih telah berbelanja di toko Kholish! ")

else:
    print("\nKeranjang kosong. Tidak ada transaksi dilakukan.")
