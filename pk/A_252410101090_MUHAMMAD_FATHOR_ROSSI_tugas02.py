print('Tugas Praktikum Pertemuan 03 \n ')


print('=' * 8 ,"No .1", "=" * 8)

ebuahString = "glegandaloblkasf" 
# #  output = flag 

print(ebuahString)
print(ebuahString[::-4], '\n')


print('=' * 8 ,"No .2", "=" * 8)

a = []
b = [3,6,9,10,8,5,7]
c = [1,3,5,7,2,4,6,8]

#poin 1 (cara concatenation)
a = b + c
# print(a)

# # poin 1 (cara unpacking)
# a = [*b, *c]
# print(a)

# poin 1 (cara extend)
# a = b.extend(c) | untuk operasi data type squence ga bisa langsung di masukkan ke dlm variabel
# b.extend(c)
# a = b
# print(a)

# poin 2 (angka duplikat tidak ditampilkan)| result tidak menjamin urutan
hai = list(set(a))

# print(hai)

# poin 3 (urutkan berdasrkann nilai)
hai.sort()
# print(hai, '\n )


print('=' * 8 ,"No .3", "=" * 8)

# data_Asprak = ['sebuah adit', 'king kholis', 'paduka wildan', 'maharaja fahmi']
# data_Asprak.reverse()
# print(str(data_Asprak)[::-1] )

data_Asprak = ['sebuah adit', 'king kholis', 'paduka wildan', 'maharaja fahmi']
data_Asprak1 = data_Asprak[0] [:: -1], data_Asprak[1] [:: -1], data_Asprak[2][:: -1]
print(data_Asprak1) 




# asprak = []
# for a in data_Asprak:
#     asprak.append (a[:: -1])
# print(asprak)
# format
# create new empty variable
# loop tiap elemen (bisa for, while)
# tambahkan eksprsi yg diinginkan(kamu menginginkan apa di variable baru itu)

#---------------------
# alo = [[a[::-1]] for a in data_Asprak]
# print(alo)
# format list comprehension
# [<ekspresi> for <item> in <iterable>]
# <iterable> = data yang mau di-loop 
# <item> = variabel tiap elemen 
# <ekspresi> = apa yang mau kamu simpan ke list baru 