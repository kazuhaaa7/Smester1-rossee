hai =  175
print("loremojodhau %d cm " % hai) # %d, d for decimal integer | basis 10 | % akan bertambah bila variable lebih dari 1

hai1 = "fathor rososi"
print("lojerhknsjf %s " % hai1) # %s, s for string |% akan bertambah bila variable lebih dari 1

# hai2 %o, o for octal | pelajari lagi ini | ip addres adlh bil octal | basis 8 = 0,1,2,3,4,5,6,7
# [<variable> : 3f]


# .capitalize() | mengubah setiap awal kalimat menjadi kapital(bila ada kata dgn kondisi kapital semua, maka akan menjadi kecil semua)
# .upper() | mengubah semua karakter menjadi kapital

#  .lower() | mengubah semua karakter menjadi non-kapital

#  .isalnum() untuk mengechek apakah terdiri simbol/ spasi(angka dan huruf)  | karakter/ simbol hasilnya akan False
# case: saat membuat password tanpa simbol

# .isdigit() | untuk mengechek apakah string terdiri dari angka 0--9,selain digit hasilnya akan false

# .count() | untuk menghitubg karakter dlm sebuah string | str,int, simbol, spasi


# .rjust() | untuk meratakan sytring ke kanan dan menambah spasi di sebelah kiri | .rjust(<sebanyak yg kita mau>)
# .ljust() | akan menambah spasi ke kanan
# case: -pembuatan judul 

# .len() | untuk mengechek banyaknya jumlah karakte pd sebuah stringr | termasuk spasi

# ord() bertujuan untuk mengecheck sebuah nial di dlm ASCII

# chr() | untuk mengubah nilai ASCII menjadi nilai awal

# hai = 65,45 # error apa bila valuenya > 1
# print(chr(hai))

# operator penugasan = +=, -+, *=, /=, //=, **=, %= |berlaku ga hanya type int

#  priortas operasi
#  tanda kurung
# eksponen
# perkalian, pembagian, modulus, floor division,
# penjumlahan dan pengurangan


# operator keanggotaan (in, not in) mengechek apakah ada value di suatu list
 
# operator logika(or, and, not, xor)
#  case perkondisian: if, else

tMenit = int(input("masukan menit yg kamu inginkan :"))
wildan = tMenit * 7
amel = int(tMenit * 8) # salah di operasi data boy
if wildan > amel :
    print(f" wildan makan bakso sebanyak {wildan} bakso  per menit , dan amel memakan bakso sebanyak {amel} bakso per menit. ")
    print(f" pemenangnya adalah wildan ")
else:
    print(f" wildan makan bakso sebanyak {wildan} bakso  per menit , dan amel memakan bakso sebanyak {amel} bakso per menit. ")
    print(f" pemenangnya adalah amel")


# .enumerate() untuk memasukka indeks ke variabel sementara





