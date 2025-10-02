# # Program (1)
# for i in range(1, 50, 2):
#     print(f'{i} ' '', end= '' '\n')    

# Program (2)
# angka = int(input("Masukkan angka:"))
# indeks = 1
# i = 1

# for i in range (1,angka + 1 ):
#     indeks *= i
# print(indeks)

# while i <= angka:
#     indeks *= i
#     i +=1
# print(indeks)

# program 3
# angka = int(input("Masukkan angka "))
# # for i in range(1, angka + 1):
# #     print("*" * i)


# # for i in range (angka, 0, -1):
# #     print("*" * i)

# tinggi = int(input("Masukkan tinggi segitiga: "))

# for i in range(tinggi):
#     spasi = " " * (tinggi - i - 1)
#     bintang = "*" * (2 * i + 1)
#     print(spasi + bintang + spasi)

# /program 4

# n = int(input("Masukkan angka"))
# for angka in range(1, n+ 1, ):
#     prima = True
#     for i in range(2, angka):
#         if angka % i :
#             prima = False 
#             break
#     if prima:
#         print(angka, end= "")

        




# program 5
# angka = int(input("Masukkan bebrapa angka: "))
# indeks = 1

# while indeks <= angka:
#     angkamasuk = int(input(f"Masukkan bilangan ke- {indeks} :"))
#     angkamasuk += angkamasuk
#     indeks += 1

# rata = int(angkamasuk / angka)
# print(rata)
