suhu = [28,30, 34, 34]
curahHujan = [200,250, 300]

for i in range(len(suhu)):
    for j in range(len(curahHujan)):
        hasilPanen = (suhu[i] * 0.15) + (curahHujan[j] * 0.08 )
        print(f"suhu: {suhu[i]}C , curah hujan: {curahHujan[j]}mm, prediksi hasil panen : {hasilPanen} ton")


# bintangterbaik = int(input("Kamu ingn melihat bintang terbalik? masukkan angka dulu, hehe :"))
# i = 0

# # bintang bawah ke atas
# # for i in range(bintangterbaik, 0, -1):
# #     print("*" * i)
                    
# # bintang dari atas ke bawah
# # while i <= bintangterbaik:
# #     print("*" * i)
# #     i += 1

# # bintang dari bawah ke atas
# while  bintangterbaik >= i:
#     print("*" * bintangterbaik)
#     bintangterbaik -= 1

# exercise nesteed loop, bu ifriina

# nBarang = int(input("Masukkan banyak barang yang kamu inginan: "))
# print("banyak barang yg dibeli", nBarang)
# hargaPerBarang = int(input("Masukkan harga per barang: "))
# print("harga barang yg dibeli per barang", hargaPerBarang)

# subtotal = nBarang * hargaPerBarang
# totalKeseluruhan = 0
# totalKeseluruhan += subtotal

# bertanya = input("Apakah ada lagi item barang yg mau dientrikan atau tidak [y]/[t] :").lower()

# while bertanya == "y"or bertanya != "t" :
#     if bertanya == "y":
#         nBarang = int(input("Masukkan banyak barang yang kamu inginan: "))
#         print("banyak barang yg dibeli", nBarang)
#         hargaPerBarang = int(input("Masukkan harga per barang: "))
#         print("harga barang yg dibeli per barang", hargaPerBarang)
#         subtotal = nBarang * hargaPerBarang
#         totalKeseluruhan += subtotal

#         bertanya = input("Apakah ada lagi item barang yg mau dientrikan atau tidak [y]/[t] :").lower()
#     elif bertanya == "t":
#         tutup = print("Baik, akan kami tutup")
#         break
#     else:
#         print("Jawaban yg kamu berikan di luar kendali kami")
#         break
    
    

# print("total jumlah yg harus dibayar: Rp", totalKeseluruhan)