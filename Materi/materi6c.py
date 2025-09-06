print("Materi 6C - Python Data Structures")
print("----------------------------------")
# List -> [ ] -> berurutan, berubah, boleh duplikat
daftar_belanja = [
  "pisang kembung",
  "es teh desa",
  "gabin"
]
print("Tas Belanja:", daftar_belanja)
# akses item dengan index
print(daftar_belanja[1])
# append() untuk menambah item ke akhir list
daftar_belanja.append("tahu goolek")
# insert() untuk menambah item ke index tertentu
daftar_belanja.insert(1, "batagor")
# remove() untuk menghapus item
daftar_belanja.remove("es teh desa")
print("Tas Belanja Skrg:", daftar_belanja)
# menggabungkan list dengan +
jajanan_ishaq = ["olive chicken", "macaroni", "keripik singkong"]
jajanan_bilal = ["naspad kawan lamo", "indomie", "gorengan"]
titip_belanjaan = jajanan_bilal + jajanan_ishaq
print("Titipan belanja:", titip_belanjaan)
# menggandakan item list dengan *
print("Bilal nambah:", jajanan_bilal * 3)

# List bercabang (list multi dimensi)
daftar_menu = [
  ["Kopi", "Teh", "Susu Jahe"], # baris 0
  ["Jus Apel", "Jus Jeruk", "Jus Alpukat", "Jus Mangga"], # baris 1
  ["Es Teler", "Es Dawet"], # baris 2
]
print("DAFTAR MENU: ",daftar_menu)
print(daftar_menu[1][2])
print('------------------')
# Tuple -> ( ) -> berurutan, tidak berubah, boleh duplikat
ttl = ("Purworejo", 21, "Januari", 2009)
print("TTL: ", ttl)
print("Bulan lahir ujang:", ttl[2])
# unpacking variable (mengekstrak tuple ke variable baru sesuai urutan)
tempat_lahir, tgl_lahir, bln_lahir, thn_lahir = ttl
print("Thn lahir: ", thn_lahir)

voting = [
  ["bilal", 0],
  ["tegar", 3],
  ["abdul", 3],
]
print("Hasil voting: ", voting)