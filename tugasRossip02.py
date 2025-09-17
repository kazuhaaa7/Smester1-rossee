# Pengiriman Paket
Tujuan = input("Kemana kah tujuan anda (Domestik/Internasional): ")
Tujuan1 = Tujuan.capitalize()

Zona = input("Kemana kah Zona yg ingin anda tuju (Jawa/Luar Jawa/Asia Tenggara/Benua Lain): ") 
Zona1 = Zona.capitalize()

zona_valid = ["Jawa", "Luar jawa", "Asia tenggara", "Benua lain"]
if Zona1 not in zona_valid :
    print(f"Zona Paket '{Zona1}' Tidak Valid ")
    # exit()
    quit()

Barang = int(input("Masukkan berat barang(kg): "))


#Tujuan

if Tujuan1 == "Domestik" :

    if Zona1 == "Jawa":
        if Barang <=5 :
            total = Barang * 6000
            print(f"""
            Tujuan Pengiriman Paket: {Tujuan}
            Zona Pengiriman Paket {Zona}
            Berat Baranf = {Barang}
            Harga per kg = Rp. 6000
            Total Biaya Pengiriman = {total}    
            """)
        else:
            print(Barang)
    elif Zona1 == "Luar Jawa ":
        if Barang <=5 :
            total = Barang * 10000
            print(f"""
            Tujuan Pengiriman Paket: {Tujuan}
            Zona Pengiriman Paket {Zona}
            Berat Baranf = {Barang}
            Harga per kg = Rp. 10.000
            Total Biaya Pengiriman = {total}    
            """)
        else:
            print(Barang)
    
    elif Zona1 == "Jawa":
        if Barang > 5 :
            total = Barang * 5000
            print(f"""
            Tujuan Pengiriman Paket: {Tujuan}
            Zona Pengiriman Paket {Zona}
            Berat Baranf = {Barang}
            Harga per kg = Rp. 5000
            Total Biaya Pengiriman = {total}    
            """)
        else:
            print(Barang)
    elif Zona1 == "Luar Jawa ":
        if Barang > 5 :
            total = Barang * 8500
            print(f"""
            Tujuan Pengiriman Paket: {Tujuan}
            Zona Pengiriman Paket {Zona}
            Berat Baranf = {Barang}
            Harga per kg = Rp. 8.500
            Total Biaya Pengiriman = {total}    
            """)
        else:
            print(Barang)
 

elif Tujuan1 == "Internasional":

    if Zona1 == "Asia Tenggara":
        if Barang <= 5:
            total = Barang * 40000
            print(f"""
            Tujuan Pengiriman Paket: {Tujuan}
            Zona Pengiriman Paket {Zona}
            Berat Baranf = {Barang}
            Harga per kg = Rp. 40.000
            Total Biaya Pengiriman = {total}    
            """)
        else:
            print(f"Harga barang {Barang}")

    elif Zona1 == "Benua Lain":
        if Barang <= 5:
            total = Barang * 75000
            print(f"""
            Tujuan Pengiriman Paket: {Tujuan}
            Zona Pengiriman Paket {Zona}
            Berat Baranf = {Barang}
            Harga per kg = Rp. 75.000
            Total Biaya Pengiriman = {total}    
            """)
        else:
            print(f"Harga barang {Barang} ")    

    elif Zona1 == "Asia Tenggara":
        if Barang > 5:
            total = Barang * 35000
            print(f"""
            Tujuan Pengiriman Paket: {Tujuan}
            Zona Pengiriman Paket {Zona}
            Berat Baranf = {Barang}
            Harga per kg = Rp. 35.000
            Total Biaya Pengiriman = {total}    
            """)
        else:
            print(f"Harga barang {Barang}")

    elif Zona1 == "Benua Lain":
        if Barang > 5:
            total = Barang * 68000
            print(f"""
            Tujuan Pengiriman Paket: {Tujuan}
            Zona Pengiriman Paket {Zona}
            Berat Baranf = {Barang}
            Harga per kg = Rp. 68.000
            Total Biaya Pengiriman = {total}    
            """)
        else:
            print(f"Harga barang {Barang} ")    
