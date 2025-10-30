# perulangan ada 2, yaitu for dan while
hai =["rossi", "lutza", "nabil", "ayu","fia", "kiya", "err"]
x = 0
while x < len(hai) :
    print(hai[x]) 
    x +=1
# bagaimana while berjalan, panjang var hai adalah 6. masuk ke while, apabila perkondisian x < panjang var hai maka akan dieskeskusi apa. += 1, artinya apabila sudah masuk tahap eksekusi maka nilai var x akan ditambah 1. program ini akan terus berlanjut hingga x < panjang var hai

harga = 5
per_harga = 1000
# if harga == 5:
#     barang1 = input("Apakah ada lagi item barang yg dientrikan atau tidak? [y]/[t] :")
#     if barang1 == "y":
#         print("yess")
#     elif barang1 == "t":
#         print("NOOO")
#     else:
#          barang1 = input("Apakah ada lagi item barang yg dientrikan atau tidak? [y]/[t] :")
# else:
#     print("G relevan")


while harga == 5: 
    barang1 = input("Apakah ada lagi item barang yg dientrikan atau tidak? [y]/[t] :")
    if barang1 == "y":
        print("yess")
    elif barang1 == "t":
        print("NOOO")
    else:
        break
    