# nomer 1
print("=" * 10 ,"Nomer 1", "=" * 10)
awal = input("Masukan nama awal kamu: ")
tengah = input("Masukan nama tengah kamu: ")
akhir = input("Masukan nama akhir kamu: ")
nim = input("Masukan NIM  kamu: ")
print(f"Selamat datang di Program Studi Sistem Informasi, {awal} {tengah} {akhir} derngan NIM: {nim} ")


# nomer 2
print("\n","=" * 10 ,"Nomer 2" ,"=" * 10)
err = int(input("Masukkan jari jari: "))
pi = 3.14

luasLingkaran = pi * err ** 2
print(f"luas lingkaran = {luasLingkaran}")
kelilingLingkaran = 2 * pi * err
print(f"keliling lingkaran {kelilingLingkaran}")




# nomer 3
print("\n","=" * 10, "Nomer 3" ,"=" * 10)
barang_satu = int(input("Masukkan harga barang satu: "))
barang_dua = int(input("Masukkan harga barang dua: "))
barang_tiga = int(input("Masukkan harga barang tiga: "))
totalAwal = barang_satu + barang_dua + barang_tiga
print(f"total sebelum mendapatkan diskon: {totalAwal}")
totalDiskon = int((barang_satu + barang_dua + barang_tiga) * 0.10)
totalDiskon2 = totalAwal - totalDiskon
print(f"total setelah mendapatkan diskon: {totalDiskon2}")