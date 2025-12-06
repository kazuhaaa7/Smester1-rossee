# # ini materi dari pertmuan 1 hingga sebelum uts
# dalam python terdiri bererapa operator:
# 1. operator aritmatika
#  -, +, *, **, /, //(pembulatan, ke bawah), %(modulo atau mencari sisa pembagian) , ^
# 2. operator penugasan atau increment
# +=, *=, **=, -=, /=, %=, //=, 6= 
# 3. operator keanggotaan
# in, not in
# 4. operator logika
# not, or, and, xor,

# -----------------------------------------------------------------------------------------
# penggabungan string atau atribut tambahan string:
# 1. +, ex= var1 + var2
# 2. "".join(), memberikan atribut tambahan pd STRING bisa berupa spasi, koma, dll
# 3.format f string, HANYA BISA DI TERPKAN APABILA STYPE STRING
# -----------------------------------------------------------------------------------------
# operasi data list:
# 1. .append() => menambah suatu value di indeks paling akhir
# 2. .insert(idx, 'valuenya') => menambah suatu value dan bisa diletakkan di mana aja
# 3. .remove(<'value dari list yang ingin dirmv' >) => meremove nilai yang diinginkan pd list
# 4. .pop(idx) => menghapus nilai dengan indeks pd list, tergantung konteks: apabila dlm data .pop() digunakan untuk mengambil data
# 5. .extend() => untuk menggabungkan beberapa list
# 6. del <nama var>[] => untuk mengahppus value pd list lewat indks
# 7. .reverse() => untuk mmebalik urutan value| bisa juga berbentuk reverse=true or false
# 8. .clear() => menghapus semua value 
# 9. .sort() => untuk mengurutkan abjad awal kata value
# 10. set() => tipe data koleksi seperti list atau tuple, tapi:
# Tidak menyimpan urutan
# Tidak boleh ada elemen ganda (otomatis unik)
# Bisa melakukan operasi himpunan (union, intersection, difference)
# otput: data bertype set
# 11. # <nm var>.count(<value yg ingin dihitung keberadaanya>) => digunakan untuk menghitung berapa kali suatu nilai muncul di dalam list, string, atau tuple.
# 12. key= | digunakan sbg acuan, biasanya dikombinasi dngn len() dan sort()| sort(key=len) akan mensortir berdasrkan banyaknya elemen 

# -----------------------------------------------------------------------------------------
# akses list:
# 1. <namavar>[]
# 2. multiplelist: <namavar> [baris][ko]
# 3. slicing list: {namavar[: : :]}
# 4. mengubah value list: <namavar[indeks]> = "isi pengganti value"

# -----------------------------------------------------------------------------------------
# slicing bisa dipakai di:
# 1. list
# 2. tuple
# 3. string

# -----------------------------------------------------------------------------------------
# casting:
# 1. type()
# 2. float()
# 3. int()
# 4. str()

# -----------------------------------------------------------------------------------------
# operator format string:
# 1. %d => decimal int
# 2. %s => string
# 3. %0 => octal int atau basis 8

# -----------------------------------------------------------------------------------------
# str unicode:
# 1. .capitalize()
# 2. .upper()
# 3. .lower()
# 4. .title()
# 5. .isalnum() => mengecek string apakah hanya terdiri dari alfanumerik yaitu karakter dan angka.
# 6. .isdigit() => Untuk mengecek string apakah hanya terdiri dari digit, yaitu angka 0 - 9.
# 7. .islower()
# 8. .isupper()
# 9. .rjust() => Untuk meratakan string ke kanan dan menambah spasi di sebelah kiri.
# 10. .ljust() => Kebalikan dari rjust
# 11. ord(() => Untuk mengubah sebuah karakter menjadi nilai numerik yang merepresentasikannya (ASCII Number).
# 12. chr() =>  Digunakan untuk mengonversi nilai integer (yang mewakili kode Unicode) menjadi karakter string tunggal.

# -----------------------------------------------------------------------------------------
# operator NOR(not or)
# 1. not (x or y)
# 2. not (x and y)
# 3. xor: c = a ^ b
# # c = (a or b) and (not (a and b))
# 4. xnor: not (a ^ b )

# -----------------------------------------------------------------------------------------
# match - case => better buat ilihan menu

# -----------------------------------------------------------------------------------------
# operasi komparasi: 
# 1. ==
# 2. >
# 3. <
# 4. >=
# 5. <=
# 6. !=
# -----------------------------------------------------------------------------------------
# operator kondidsi:
# 1.if - elif - else
# 2. nested if => if bersarang
# 3. ternary operator: <nilai_jika_benar> if <kondisi> else <nilai_jika_salah>

# -----------------------------------------------------------------------------------------
# looping atau iterasi
# 2. while => digunakan saat tidak diketahui yang akan diiterasi sebanyak apa
# 2. for => digunakan saat mengetahui brp bnya yang akan diiterasi

# -----------------------------------------------------------------------------------------
# kontrol loop:
# 1. break => akan memberhentikan program
# 2. continue => akan men-skip program
# -----------------------------------------------------------------------------------------

# list comprehension: cara singkat dan efisien untuk membuat list baru dari list (atau iterable) lain dengan menuliskan ekspresi dalam satu baris kode
# -----------------------------------------------------------------------------------------

### FUNGSI
# Parameter => nilai yang dikirimkan ke dalam fungsi saat dipanggil — seperti input data yang ingin kamu olah. dan bisa diisi dgn argumen bebas.
# return => ntuk mengembalikan hasil ke pemanggil fungsi.
# Tanpa return, fungsi tidak mengembalikan apa pun (secara default nilainya None).
# Scope => menentukan di mana variabel bisa digunakan.
# Ada dua jenis utama: Global dan Local
# Global bisa diakses di seluruh program, di luar fungsi
# Local hanya bisa diaksss lewat funcion aja, var diletakkan atau dideklarasikan di alm pyhton.
# Lambda => cara singkat untuk menulis fungsi sederhana — biasanya hanya satu baris.
# bentuk umum => <var> = lambda parameter: ekspresi
# bisa digunakan di fungsi:
# map() → fungsi yg menerapkan fungsi ke setiap elemen list. sepahamku, fungsi ini bisa melakukan hal yg tidak biasa, contoh klo ada value yg bertype int lalu kita masukkan ke fungsi yg khsusus type str itu bakalab error, jadi solusinya apabila itu terjadi bisa pake map(). at least memiliki 2 argument
# filter() → menyaring data dengan kondisi tertentu
# sorted() → mengurutkan berdasarkan kriteria tertentu
# any() itu untuk mengecek apakah ADA minimal SATU elemen dalam iterable yang bernilai True.
# sum() adalah built-in function dalam Python yang digunakan untuk menjumlahkan semua elemen dalam sebuah iterable (seperti list, tuple, dll).
# len() adalah fungsi built-in Python yang digunakan untuk menghitung panjang atau jumlah elemen dari sebuah objek. => target: data y typenya list, str, dict. selain int dan float. 
# range() adalah fungsi yang menghasilkan urutan angka yang biasa digunakan untuk perulangan.target: int
# kombinasi range(len(<var yg valuenya bertype list, str, dict>))
# .replace() => digunakan untuk mengganti (replace) suatu teks lama dengan teks baru dalam string.
# -----------------------------------------------------------------------------------------

### COMPREHENSION DAN GENERATOR
# List comprehension adalah cara singkat untuk membuat list baru dari data lain (seperti list, range, string, dll), hanya dalam satu baris kode.
# contoh format => <nam var> = [ekspresi | for item in iterable | if kondisi]
# Generator mirip dengan list comprehension, tapi lebih hemat memori
# Bedanya:
# List comprehension → menyimpan semua hasil di memori.
# Generator → menghasilkan satu per satu (lazy) saat dibutuhkan. => outpunya berupa generator object. klo mau periksa valuenya, coba pake looping
# -----------------------------------------------------------------------------------------

### EROR HANDLING(try, except)
# Error handling itu cara Python menangani kesalahan saat program dijalankan.
# Biasanya, kalau ada error (misalnya salah bagi angka dengan nol, atau input yang bukan angka), program langsung berhenti total dan keluar pesan merah panjang.
# Nah, biar program nggak berhenti mendadak, kita bisa menangkap error-nya pakai try dan except.
# ada 2 blok tmabahn selain try, except (opsional):
# try:
#     # coba jalankan | Tempat kode yang bisa bikin error
#except:
#     # kalau error | Tangani kalau error terjadi
# else:
#     # kalau TIDAK error | Jalan kalau tidak error
# finally:
#     # akan jalan SELALU (error atau nggak) | bakal Selalu jalan meskipun (error atau tidak), 
# jdi klo mau pake blok kode else: di blok kode try: ga usah di kasi print atau cetak hasil apapun ketika programnya tdk error


# -----------------------------------------------------------------------------------------
# hai2 %o, o for octal | pelajari lagi ini | ip addres adlh bil octal | basis 8 = 0,1,2,3,4,5,6,7

# -----------------------------------------------------------------------------------------
# [<variable> : 3f]


# -----------------------------------------------------------------------------------------
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
# -----------------------------------------------------------------------------------------

# operator penugasan = +=, -+, *=, /=, //=, **=, %= |berlaku ga hanya type int

#  priortas operasi
#  tanda kurung
# eksponen
# perkalian, pembagian, modulus, floor division,
# penjumlahan dan pengurangan
# -----------------------------------------------------------------------------------------


# operator keanggotaan (in, not in) mengechek apakah ada value di suatu list
# operator logika(or, and, not, xor)
#  case perkondisian: if, else
# -----------------------------------------------------------------------------------------

# materi data handling
# colums = <[nama header colom]> | digunakan jika ingin memberi nama pada suatu kolom
# .shape(), untuk menampilkan ukuran df => brp baris dan brp kolom
# len(<var dataframe>), digunakan untuk membaca banyaknya data dgn hitungan idx.
# .describe() untuk membaca detail dara data, terdiri dari count,mean,std, min, 25%, 50%, 75%,dan max ini tergantung banyaknya data
# .info(untuk meriksa apakah ada missing value pd data), pandas
# untuk membaca kolom tertentu terdapat 2 cara:
# df["<nama kolom>"] atau df.<nama kolom>
# format untuk membaca sel terntu dari suatu kolom: .iloc[baris,kolom], bisa pake slicing juga
# iloc = integer location based idx| untuk mengasksesnya berdasrakan posisinya objek [baris, kolom],yg dimana dia bisa diakses hanya dengan indeks
# loc = location| untuk mengakses berdasarkan label indeks [baris ke brp/ idx , nama kolom ], dia bisa diakses lewat indeks dan nama kolom 
# -----------------------------------------------------------------------------------------

# #MANIPULASI DATA |CRUD
# manipulasi data: join(base on index), concat(base on idx) bedanya ada di axis=, 1 apabila beberapa data ingin digabung, klo axis= 0, akan menambah baris dan colom  menummpuk data yg sudah ada, merge = > sifat siftnya yg komplex
# join() - Bergabung Berdasarkan Index
# Karakteristik:
# Berdasarkan: Index (default)
# Tipe join: Left join (default)
# Use case: Menggabungkan DataFrame berdasarkan index
# Parameter penting:
# how: 'left', 'right', 'inner', 'outer'
# lsuffix, rsuffix: Suffix untuk kolom duplikat

# concat() - megambil value dri beberapa variabel. Vertikal/Horizontal
# Karakteristik:
# Berdasarkan: Axis (0=vertical, 1=horizontal)
# Tipe: Stacking/concatenation
# Use case: Menggabungkan DataFrame dengan struktur serupa
# Parameter penting:
# axis: 0 (vertical), 1 (horizontal)
# ignore_index: tidak memperlihatkan index
# keys: Multi-index untuk identifikasi source

# merge() - SQL-style Join
# Karakteristik:
# Berdasarkan: Kolom tertentu (bukan index)
# Tipe join: Inner join (default)
# Use case: Menggabungkan seperti SQL JOIN
# Parameter penting:
# on: Kolom untuk join
# how: 'inner', 'left', 'right', 'outer', 'cross'
# left_on, right_on: Kolom berbeda antara DataFrame

# .iloc[bisa pakai idx atau nama kolom] => untuk memanipulasi value 
# .drop(nomer brp, memakai numerik manusia) => menghaous value 
# .index => mendefinisikan nilai idx ke df
# .at[<baris idx brp>, <nama kolom>] = <value yg ingin diubah>
# -----------------------------------------------------------------------------------------

# #BEKERJA DGN FILE
# masih berlaku aturan file handling
# menyimpan data ke dalam csv, .to_csv(<nama fie>)

# $apabila ada data null dan bernilai dgn numerik bbisa disi dgn nilai mean
# $apbila kategorikal bisa diganti dgn modus