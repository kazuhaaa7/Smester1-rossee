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

# penggabungan string atau atribut tambahan string:
# 1. +, ex= var1 + var2
# 2. "".join(), memberikan atribut tambahan pd string bisa berupa spasi, koma, dll
# 3.format f string

# operasi data list:
# 1. .append() => menambah suatu value di indeks paling akhir
# 2. .insert() => menambah suatu value dan bisa diletakkan di mana aja
# 3. .remove(<value dari list yang ingin dirmv >) => meremove nilai yang diinginkan pd list
# 4. .pop() => menghapus nilai dengan indeks pd list
# 5. .extend() => untuk menggabungkan beberapa list
# 6. del <nama var>[] => untuk mengahppus value pd list lewat indks
# 7. .reverse() => untuk mmebalik urutan value
# 8. .clear() => menghapus semua value 
# 9. .sort() => untuk mengurutkan abjad awal kata value
# 10. set() => tipe data koleksi seperti list atau tuple, tapi:
# Tidak menyimpan urutan
# Tidak boleh ada elemen ganda (otomatis unik)
# Bisa melakukan operasi himpunan (union, intersection, difference)
# 11. # <nm var>.count(<value yg ingin dihitung keberadaanya>) => digunakan untuk menghitung berapa kali suatu nilai muncul di dalam list, string, atau tuple.

# akses list:
# 1. <namavar>[]
# 2. multiplelist: <namavar> [][]
# 3. slicing list: {namavar[: : :]}
# 4. mengubah value list: <namavar[indeks]> = "isi pengganti value"

# slicing bisa dipakai di:
# 1. list
# 2. tuple
# 3. string

# casting:
# 1. type()
# 2. float()
# 3. int()
# 4. str()

# operator format string:
# 1. %d => decimal int
# 2. %s => string
# 3. %0 => octal int atau basis 8

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

# operator NOR(not or)
# 1. not (x or y)
# 2. not (x and y)
# 3. xor: c = a ^ b
# # c = (a or b) and (not (a and b))
# 4. xnor: not (a ^ b )

# match - case => better buat ilihan menu

# operasi komparasi: 
# 1. ==
# 2. >
# 3. <
# 4. >=
# 5. <=
# 6. !=
# operator kondidsi:
# 1.if - elif - else
# 2. nested if => if bersarang
# 3. ternary operator: <nilai_jika_benar> if <kondisi> else <nilai_jika_salah>

# looping atau iterasi
# 2. while => digunakan saat tidak diketahui yang akan diiterasi sebanyak apa
# 2. for => digunakan saat mengetahui brp bnya yang akan diiterasi

# kontrol loop:
# 1. break => akan memberhentikan program
# 2. continue => akan men-skip program

# list comprehension: cara singkat dan efisien untuk membuat list baru dari list (atau iterable) lain dengan menuliskan ekspresi dalam satu baris kode

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
# map() → menerapkan fungsi ke setiap elemen list
# filter() → menyaring data dengan kondisi tertentu
# sorted() → mengurutkan berdasarkan kriteria tertentu

### COMPREHENSION DAN GENERATOR
# List comprehension adalah cara singkat untuk membuat list baru dari data lain (seperti list, range, string, dll), hanya dalam satu baris kode.
# contoh format => <nam var> = [ekspresi | for item in iterable | if kondisi]
# Generator mirip dengan list comprehension, tapi lebih hemat memori
# Bedanya:
# List comprehension → menyimpan semua hasil di memori.
# Generator → menghasilkan satu per satu (lazy) saat dibutuhkan. => outpunya berupa generator object. klo mau periksa valuenya, coba pake looping

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
