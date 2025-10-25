# ===================================================================================
# no 1
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
