# no 1✅
# sample 0✅
ntotal = 0
tampungan = []
while True:
    hai = int(input("jumlah barang yg dibeli: "))

    for i in range( hai):
        harga = float(input("masukkan harga tiap barang: "))
        i += 1
        ntotal += harga
    print(ntotal)
    break
# sample 1✅
ntotal = 0
tampungan = []
while True:
    hai = int(input("jumlah barang yg dibeli: "))

    for i in range( hai):
        harga = float(input("masukkan harga tiap barang: "))
        i += 1
        ntotal += harga
    print(ntotal)
    break
# ===================================================================================

# no 2/ error, harus menggubaan looping
daftar = ['RotiNaga', 'SupElf', 'RotiNaga', 'SupElf', 'RotiNaga', 'JusPhoenix']
palingMenu = max(daftar, key=daftar.count)
print(" ".join(daftar))
print(palingMenu)

# ==============
# solusi menggunakan loop dan dict sbg tampungan
# ==============

daftar = ['RotiNaga', 'SupElf', 'RotiNaga', 'SupElf', 'RotiNaga', 'JusPhoenix']
# Buat dictionary kosong untuk menyimpan jumlah tiap item
hitung = {}

# Looping untuk menghitung kemunculan
for item in daftar:
# program akan periksa satu per satu. 
    if item in hitung:
        hitung[item] += 1
    else:
        hitung[item] = 1
# Kalau nama menu sudah ada di var hitung, tambahkan jumlahnya (+1).
# Kalau belum ada, buat entri baru dengan nilai 1.

# Sekarang cari item dengan jumlah terbanyak
palingMenu = None #karna blm tau menu apa yg sering digunakan, bakalan ditimpa setelah diiterasi
jumlahTerbanyak = 0
# Awalnya, belum tahu menu mana yang paling sering, jadi diset kosong dulu (None)

for item, jumlah in hitung.items():
    if jumlah > jumlahTerbanyak:
        jumlahTerbanyak = jumlah
        palingMenu = item

# Cetak hasil
print(" ".join(daftar))
print(palingMenu)

# ================
# solusi menggunakan .count dan set()
# ================

daftar = ['RotiNaga', 'SupElf', 'RotiNaga', 'SupElf', 'RotiNaga', 'JusPhoenix']

palingMenu = "" # bisa diganti "None"
jumlahTerbanyak = 0

for item in set(daftar):  # set() biar tiap item unik
# set(daftar) akan menghapus duplikat dari daftar.
    if daftar.count(item) > jumlahTerbanyak:
    # .count(x) digunakan untuk menghitung berapa kali suatu nilai x muncul di dalam list.
        jumlahTerbanyak = daftar.count(item)
        palingMenu = item

print(" ".join(daftar))
print(palingMenu)


# ===================================================================================

# no 3// perbedaan sort dan sorted lalu beri list yg berisi indeks
# n = int(input("banyak kata yg akan ditulis oggy"))
# hai = []
# for i in range(1, n + 1):
#     kata = input("masukkan kata apa aja").lower()
#     hai.append(kata)
#     ascii = [ord(i) for i in kata]
#     char = [chr(x) for x in ascii]
#     unik = set(char)
#     loh = sorted(unik)
#     # perbedaan sorted dan sort

# print("".join(loh))
# print(",".join(hai))

# ===================================================================================

# no 4✅
# hai = 6
# for i in range(1, hai+1):
#     if i % 3 == 0:
#         print("#" * i)
#     else:
#         print("*" * i)

# ===================================================================================

# no 5✅
# kataSandi = int(input("Masukkan beberapa kata sandi yg akan diuji: "))
# tampungan = []

# for i in range(1, kataSandi + 1 ):
#     inputKatasandi = input("Masukkan kata sandi")
#     mypoin = 0
# # knp aku bikin if banyak kali? 
# # Karena kamu pakai elif, maka hanya satu kondisi pertama yang benar akan dijalankan.
# # Padahal kamu ingin semua kondisi dicek (huruf besar, kecil, angka, dll).
# # Jadi harusnya pakai if semua, bukan elif.
#     if len(inputKatasandi) >= 8:
#         mypoin += 2

#     if any(char.isupper() for char in inputKatasandi):
#         mypoin += 1

#     if any(char.islower() for char in inputKatasandi):
#         mypoin += 1

#     if any(char.isdigit() for char in inputKatasandi):
#         mypoin += 1

#     if any(not char.isalnum() for char in inputKatasandi):
#         mypoin += 2
    
#     tampungan.append(inputKatasandi)

#     if mypoin >=6 :
#         kategori = "Masuk kategori KUAT"
#     elif mypoin >=4 :
#         kategori = "Masuk kategori SEDANG"
#     elif mypoin >=2 :
#         kategori = "Masuk kategori LEMAH"
#     else:
#         kategori = "Masuk kategori SANGAT LEMAH"

#     print("halo halo", kategori,"skor", mypoin)
