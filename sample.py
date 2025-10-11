# program 1: Kholish - Owner KholishShop Kholish - Owner KholishShop 

# ===========================
# PROGRAM ONLINE SHOP KHOLIF
# ===========================


# Daftar produk dan harga
produk = { 
"Iphone 20": 20000, 
"Macbook Air M4": 40000, 
"Sosis Kanzler": 35000 
}

keranjang = [] #list kosong 
subtotal = 0
ongkir = 10000
ppn = 0.12

print("=== Selamat Datang di Kholis Shop ===")
print("Kami menjual:")

for nama, harga in produk.items():
    print(f"- {nama}: Rp{harga:,}", end= "\n")

# ==============
# input barang
# ==============

while True: #Ga harus perkondisian
    
    # tampil menu produk
    jmlhprodyk = int(input("Entry jumlah barang yg kamu mau: "))
    for i in enumerate(jmlhprodyk , start=0):
        sales = input("Entry nama produk atau  ketik 'Stop' untuk lanjut ke prosedur selanjutnya  ").title()
        
        if sales == "Stop":
            print("Baik, akan kami lanjutkan ke prosedur selanjutnya ")
            print(f"Total harga barang yg kamu pilih {subsubtotalAtas}")
            break
            # prosedur penjumlahan / co
        elif sales in produk :
            jumlatiapbrg = int(input("Entry seberapa banyak barang yg kamu inginkan "))
            subsubtotalAtas = (produk[sales]) * jumlatiapbrg
            # subtotal += subsubtotal
            total = (subsubtotalAtas * Pjk) + subsubtotalAtas + ongir
            ttl = int(total)
            keranjang.append((sales,jumlatiapbrg,subsubtotalAtas))

            if i == jmlhprodyk:
                print(f"total pembelanjaan kamu setelah terkena pajak sebesar {Pjk} dan ongkir sebesar Rp.{ongir} saat ini adalah Rp.{ttl}")
                break
        else:
            print("Pilihan anda tidak ada di menu kami")
            exit() #tamabahin bisa iterasi ke awal lagi


    # # Apbila ada barang yg ingn diinputkan lagi
    nextStep = input("Apakah kamu ingin menambahkan pembelanjaan lagi? [y]/[t]: ").lower()
    while True:
        if nextStep == "y":
            jmlhprodykagain = int(input("Entry jumlah barang yg kamu mau: "))
            for x in range(1 , jmlhprodykagain +1):
                sales2 = input("Entry nama produk lagi atau  ketik 'Stop' untuk lanjut ke prosedur selanjutnya  ").title()
                
            if sales2 == "Stop":
                print("Baik, akan kami lanjutkan ke prosedur selanjutnya ")
                print(f"Total harga barang yg kamu pilih {subtotal}")
                exit()
                    # prosedur penjumlahan / co
            elif sales2 in produk :
                jumlatiapbrg = int(input("Entry seberapa banyak barang yg kamu inginkan lagi "))
                subsubtotalBawah = (produk[sales2]) * jumlatiapbrg
                # subtotal += subsubtotal
                total = (subsubtotalBawah * Pjk) + subsubtotalBawah + ongir
                ttl = int(total)
                keranjang.append((sales, jumlatiapbrg, subsubtotalBawah))
                    
                if x== jmlhprodyk:
                    print(f"total pembelanjaan kamu setelah terkena pajak sebesar {Pjk} dan ongkir sebesar Rp.{ongir} saat ini Rp.{ttl}")
                else:
                    print("Pilihan anda tidak ada di menu kami")
                    continue
        elif nextStep == "t":
            print("baik akan kami tutup")
            continue
        else:
            print("Jawaban anda tidak ada di opsi")
            continue
        print("=" * 8, "STRUK BELANJA" "=" * 8)
        print(f"iterasi ke {i} {sales} x {jumlatiapbrg} = Rp.{keranjang[i][2]}")
        if i == 2:
            print(f"iterasi ke {i} {sales} x {jumlatiapbrg} = Rp.{keranjang[i][2]}")
        print(f"iterasi ke {x} {sales2} x {jumlatiapbrg} = Rp.{keranjang[x][2]}")
        if x == 2:
            print(f"iterasi ke {x} {sales2} x {jumlatiapbrg} = Rp.{keranjang[x][2]}")
        print(f"{sales2} x {jumlatiapbrg} = Rp.{keranjang[x["subsubtotalBawah"]]}")
        print("-" * 15)
        print("Subtotal:", subsubtotalAtas + subsubtotalBawah)
        print("PPN(12%):", (subsubtotalAtas +subsubtotalBawah) * Pjk)
        print("Ongkir Rp.", {ongir})
        print("-" * 15)
        print("Total Bayar: Rp." ,{ttl})
        print(keranjang)

