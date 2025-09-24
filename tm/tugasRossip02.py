# Pengiriman Paket
Tujuan = input("Kemana kah tujuan anda? (Domestik/Internasional): ")
Tujuan_masuk = Tujuan.title()
tujuan_valid = ["Domestik", "Internasional"]
if Tujuan_masuk not in tujuan_valid :
    print(f"Tujuann Paket '{Tujuan_masuk}' Tidak Valid ")
    # exit()
    quit()

Zona = input("Kemana kah Zona yg ingin anda tuju (Jawa/Luar Jawa/Asia Tenggara/Benua Lain): ") 
Zona_masuk = Zona.title()

zona_valid = ["Jawa", "Luar Jawa", "Asia Tenggara", "Benua Lain"]
if Zona_masuk not in zona_valid :
    print(f"Zona Paket '{Zona_masuk}' Tidak Valid ")
    # exit()
    quit()

Barang = int(input("Masukkan berat barang(kg): "))
HargaperBarang = [6000, 10000, 5000, 8500,40000, 75000, 35000, 68000]


#Tujuan

if Tujuan_masuk == "Domestik" :

    if Zona_masuk == "Jawa":
        if Barang <=5 :
            total = Barang * HargaperBarang[0]
            print(f"""
            Tujuan Pengiriman Paket: {Tujuan}
            Zona Pengiriman Paket {Zona}
            Berat Barang = {Barang}
            Harga per kg = Rp.{HargaperBarang[0]}
            Total Biaya Pengiriman = {total}    
            """)
        else:
            print(Barang)
    elif Zona_masuk == "Luar Jawa ":
        if Barang <=5 :
            total = Barang * HargaperBarang[1]
            print(f"""
            Tujuan Pengiriman Paket: {Tujuan}
            Zona Pengiriman Paket : {Zona}
            Berat Baranf = {Barang}
            Harga per kg = Rp.{HargaperBarang[1]}
            Total Biaya Pengiriman = {total}    
            """)
        else:
            print(Barang)
    
    elif Zona_masuk == "Jawa":
        if Barang > 5 :
            total = Barang * HargaperBarang[2]
            print(f"""
            Tujuan Pengiriman Paket: {Tujuan}
            Zona Pengiriman Paket {Zona}
            Berat Baranf = {Barang}
            Harga per kg = Rp. {HargaperBarang[2]}
            Total Biaya Pengiriman = {total}    
            """)
        else:
            print(Barang)
             
    elif Zona_masuk == "Luar Jawa ": 
        if Barang > 5 :
            total = Barang * HargaperBarang[3] 
            print(f"""
            Tujuan Pengiriman Paket: {Tujuan}
            Zona Pengiriman Paket {Zona}
            Berat Baranf = {Barang}
            Harga per kg = Rp. {HargaperBarang[3]}
            Total Biaya Pengiriman = {total}    
            """)
        else:
            print(Barang)

    elif Zona_masuk == "Asia Tenggara":
        print(f"Daerah {Zona_masuk} tidak ditemukan di tujuan {Tujuan_masuk}") 
        exit()
   
    elif Zona_masuk == "Luar Benua":
        print(f"Daerah {Zona_masuk} tidak ditemukan di tujuan {Tujuan_masuk}") 
        exit()

elif Tujuan_masuk == "Internasional":

    if Zona_masuk == "Asia Tenggara":
        if Barang <= 5:
            total = Barang * HargaperBarang[4]
            print(f"""
            Tujuan Pengiriman Paket: {Tujuan}
            Zona Pengiriman Paket {Zona}
            Berat Baranf = {Barang}
            Harga per kg = Rp. {HargaperBarang[4]}
            Total Biaya Pengiriman = {total}    
            """)
        else:
            print(f"Harga barang {Barang}")

    elif Zona_masuk == "Benua Lain":
        if Barang <= 5:
            total = Barang * HargaperBarang[5]
            print(f"""
            Zona Pengiriman Paket {Zona}
            Berat Baranf = {Barang}
            Harga per kg = Rp. {HargaperBarang[5]}
            Total Biaya Pengiriman = {total}    
            """)
        else:
            print(f"Harga barang {Barang} ")    

    elif Zona_masuk == "Asia Tenggara":
        if Barang > 5:
            total = Barang * HargaperBarang[6]
            print(f"""
            Tujuan Pengiriman Paket: {Tujuan}
            Zona Pengiriman Paket {Zona}
            Berat Baranf = {Barang}
            Harga per kg = Rp. {HargaperBarang[6]}
            Total Biaya Pengiriman = {total}    
            """)
        else:
            print(f"Harga barang {Barang}")

    elif Zona_masuk == "Benua Lain":
        if Barang > 5:
            total = Barang * HargaperBarang[7]
            print(f"""
            Tujuan Pengiriman Paket: {Tujuan}
            Zona Pengiriman Paket {Zona}
            Berat Baranf = {Barang}
            Harga per kg = Rp. {HargaperBarang[7]}
            Total Biaya Pengiriman = {total}    
            """)
        else:
            print(f"Harga barang {Barang} ")  

    elif Zona_masuk == "Jawa":
        print(f"Daerah {Zona_masuk} tidak ditemukan di tujuan {Tujuan_masuk}") 
        exit()
  
    elif Zona_masuk == "Luar Jawa":
        print(f"Daerah {Zona_masuk} tidak ditemukan di tujuan {Tujuan_masuk}")   
        exit()

    

# ada sedikit error di sisni dan harus di solving:
# apabila input internasional tp memilih daerah yg ada di tujuan domestik itu harusnya muncul alert atau memberhentikan program sebab tidak ada tabel yg terkait itu
