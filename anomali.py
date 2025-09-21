# id_karyawan = int(input("Masukkkan 4 angka dari 1000"))


# def cek_akses(id_karyawan, jam, hari, weekend_access, mode_darurat, suhu):
#     # 1. Cek kartu akses valid
#     if not (1000 <= id_karyawan <= 9999):
#         return "Akses ditolak: kartu tidak valid"

#     # 2. Identifikasi apakah manager
#     id_str = str(id_karyawan)
#     manager = id_str.startswith("8") or id_str.startswith("9")

#     # 3. Jika mode darurat
#     if mode_darurat:
#         return "Akses ditolak: mode darurat aktif"

#     # 4. Cek suhu
#     if suhu > 38:
#         if manager:
#             return "Akses diterima: suhu tinggi tapi manager"
#         else:
#             return "Akses ditolak: suhu tidak normal"

#     # 5. Jika manager (bisa masuk kapan saja)
#     if manager:
#         return "Akses diterima: manager"

#     # 6. Cek jam kerja valid
#     jam_valid = (8 <= jam < 17) or (19 <= jam < 22)

#     # 7. Cek hari kerja
#     hari_valid = (hari in ["Senin", "Selasa", "Rabu", "Kamis", "Jumat"]) or weekend_access

#     # 8. Jika semua syarat umum terpenuhi
#     if jam_valid and hari_valid and 36 <= suhu <= 38:
#         return "Akses diterima"
#     else:
#         return "Akses ditolak"


id_karyawan = int(input("Masukkkan 4 angka dari 1000"))
jam = int(input("Masukkan jam kerja:"))
hari = input("Masukkan hari: ")
suhu = int(input("Masukkan suhu mu"))




# kondisi
def cekAkses(id_karyawan, jam, hari, suhu):
    if not (1000 <= id_karyawan <= 9999):
        return "Akses ditolak: kartu tidak valid"
    
id = str(id_karyawan)
manager = id.startswith("8") or id.startswith("9")

# mode darurat



# end


# cek suhu
if suhu > 38:
    if manager:
        print("Akses diterima: suhu tinggi bt he is manager")
    else:
        print("Akses ditolak: suhu tidak normal")


if manager :
    print("Akses diterima: manager")

jamVlid = (8 <= jam < 17) or (19 <= jam < 22)
weekendAccess= ["Sabtu", "Minggu"]
hariValid = (hari in ["Senin", "Selasa", "Rabu", "Kamis", "Jumat"]) or weekendAccess