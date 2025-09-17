# # nomer 1
# sebuahString = "glegandaloblkasf"
# # kata_tersembunyi = sebuahString[15] + sebuahString [1] + sebuahString [4] + sebuahString[3]
# print(kata_tersembunyi[::-4])
# print("output :" , kata_tersembunyi)

# # nomer 2
# a = []
# b = [3,4,5,6,7,8,9,10]
# c = [1,2,3,4,5,6,7,8]

# a = b + c
# a = set(a)
# a = list(a)

# print ("Output :", a)

# nomer 3
dataAsprak = ["sebuah adit", "king kholis", "paduka wildan", "maharaja fahmi"]
# dibalik = []
# for nama in dataAsprak:
#     dibalik.append(nama[ ::-1])
#     print(dibalik)
data_reverse = dataAsprak[0][::-1], dataAsprak[1][::-1], dataAsprak[2][::-1]
print(data_reverse)