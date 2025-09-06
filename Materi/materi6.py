print("Materi 6 - Python Data Structure")
print("--------------------------------")
# List [] (berurutan, bisa diubah, boleh duplikat)
daftar_belanja = [
  "teh desa", # index 0
  "naspad kawan lamo", # index 1
  "pisang kembung" # index 2
]
# [no_index] mengakses list lewat index
print("isi tas belanja:", daftar_belanja)
print("item ke-1:", daftar_belanja[0])
print("item ke-2:", daftar_belanja[1])
# append() menambah item baru ke akhir list
daftar_belanja.append("olive chicken")
daftar_belanja.append("gabin")
print("isi tas belanja skrg:", daftar_belanja)
print("item ke-4:", daftar_belanja[3])
# remove() menghapus item dari list
daftar_belanja.remove("pisang kembung")
print("isi tas belanja akhir:", daftar_belanja)

print(" ------ TUPLE ---------")
# tuple (berurut, tidak bisa diubah, boleh duplikat)
# penulisannya menggunakan ()
ttl = ("Bandung", 1, "Juli", 1998)
print("tgl lahir ujang:", ttl)
# [no_index] akses data tuple
print("Tempat:", ttl[0])
print("Tanggal:", ttl[1])
print("Bulan:", ttl[2])
print("Tahun:", ttl[3])
# akses bulan (posisi index) : lalu batas akhir item nya
print("Bulan tahun:", ttl[2:4])
# unpacking tuple ke variable baru
# mengikuti urutan itemnya
tempat_lahir, tgl_lahir, bulan_lahir, thn_lahir = ttl
print(tempat_lahir)

# manipulasi list lanjutan
# menggabungkan list dengan +
jajan_ujang = ["pentol", "cireng"]
jajan_asep = ["bakso", "nasgor"]
jajan_ujang_dan_asep = jajan_ujang + jajan_asep
print(jajan_ujang_dan_asep)
# list multi-dimensi (list di dalamnya ada list)
list_minuman = [
  ["kopi", "susu", "teh"], # baris 0
  ["jus apel", "jus melon", "jus jeruk"], # baris 1
  ["es teler", "es campur", "es dawet"], # baris 2
]
print(list_minuman)
# tiap baris punya 3 index (0, 1, 2)
print(list_minuman[2][1]) # akses es campur