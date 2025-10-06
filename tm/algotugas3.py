# PERLU REVISIIII
# # Program (1)
# for i in range(1, 50, 2):
#     print(f'{i} ' '', end= '' )    
#     # akan mendeteksi angka dari 1 hingga 50, tetapi dengan longkap 2

# # Program (2)
# angka = int(input("Masukkan angka:"))
# indeks = 1
# i = 1

# for i in range (1,angka + 1 ):
#     indeks *= i
# print(indeks)
# # akan mendeteksi dari angka 1 hingga angka yg sudah diinputkan. lalu saat iterasi var indeks di kali dengan var i

# # while i <= angka:
# #     indeks *= i
# #     i +=1
# # print(indeks)

# # program 3
# angka = int(input("Masukkan angka "))
# for i in range(1, angka + 1):
#     print("*" * i)


# for i in range (angka, 0, -1):
#     print("*" * i)

# tinggi = int(input("Masukkan tinggi segitiga: "))

# for i in range(tinggi):
#     spasi = " " * (tinggi - i - 1)
#     bintang = "*" * (2 * i + 1)
#     print(spasi + bintang + spasi)

# # program (4)

a = int(input("Masukkan angka: "))
for z in range(1, a+ 1):
    prima = True
    for i in range(2, z):
        if z % i == 0  :
            prima = False 
            break
    if prima:
        print(z, end=" ")

        




# program 5
angka = int(input("Masukkan bebrapa angka: "))
indeks = 1

while indeks <= angka:
    angkamasuk = int(input(f"Masukkan bilangan ke- {indeks} :"))
    angkamasuk1 = angkamasuk + angkamasuk
    indeks = indeks + 1

rata = int(angkamasuk1 / angka)
print(rata)


# angka = int(input("Masukkan bebrapa angka: "))
# indeks = 0

# for i in range (1 , angka+ 1) :
#     angkamasuk = int(input(f"Masukkan bil"))
#     indeks = indeks + angkamasuk
# rata = int(indeks / angka)
# print(rata)
