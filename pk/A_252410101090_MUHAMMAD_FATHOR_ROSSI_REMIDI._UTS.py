# ===================================================================================
# no 1
ntotal = 0
harga = [12000, 8000.5, 15000]
while True:
    for i in range(4):
        i += 1
    hargatotal = sum(harga)
    print("Total belanja :", float(hargatotal))
    break

# ===================================================================================
# no 2
daftar = ['RotiNaga', 'SupElf', 'RotiNaga', 'SupElf', 'RotiNaga', 'JusPhoenix']

palingMenu = ""
jumlahTerbanyak = 0 

for item in set(daftar): 
    if daftar.count(item) > jumlahTerbanyak:
        jumlahTerbanyak = daftar.count(item)
        palingMenu = item

print(palingMenu)

# ===================================================================================
# no 3
hai = ["apple", "banana", "apple", "cherry", "banana", "apple", "date"]

unik = []
jumlah_kemunculan = []
for i in hai:
    if i not in unik:
        unik.append(i)
        jumlah_kemunculan.append(hai.count(i))

print(len(unik))  
print(",".join(str, jumlah_kemunculan))  
# ===================================================================================
# no 4
hai = 6
for i in range(hai):
    if i % 3 == 0:
        print("#" * i)
    else:
        print("*" * i)

# ===================================================================================
# no 5
kataSandi = ['rahasia', 'Admin123', 'p4ssw0rd!', 'ADMIN']
hasil_penilaian = []
for inputKatasandi  in kataSandi:
    mypoin = 0

    if len(inputKatasandi) >= 8:
        mypoin += 2

    if any(char.isupper() for char in inputKatasandi):
        mypoin += 1

    if any(char.islower() for char in inputKatasandi):
        mypoin += 1

    if any(char.isdigit() for char in inputKatasandi):
        mypoin += 1

    if any(not char.isalnum() for char in inputKatasandi):
        mypoin += 2


    if mypoin >=6 :
        kategori = "Kuat"
    elif mypoin >=4 :
        kategori = "Sedang"
    elif mypoin >=2 :
        kategori = "Lemah"
    else:
        kategori = "Sangat Lemah"

    print(inputKatasandi, "-", kategori,)
    hasil_penilaian.append(kategori)

print("Rekapitulasi: ")
print(f"Kuat: {hasil_penilaian.count('Kuat')} ")
print(f"Sedang: {hasil_penilaian.count('Sedang')} ")
print(f"Lemah: {hasil_penilaian.count('Lemah')} ")
print(f"Sangat Lemah: {hasil_penilaian.count('Sangat Lemah')} ")