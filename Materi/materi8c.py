print("MATERI 8C - Function Basic")
print(">>>>>>>>>>>>>>>>>>>>>>>>>>>")
# buat fungsi dengan `def` lalu nama fungsi nya
# parameter `nama` untuk mengambil nilai dari luar ke isi fungsi
def halo_dunia(nama):
  print("Ohayou Minna")
  print("Hello Mr. ", nama)
  print("---------------->")

# panggil nama fungsi disertai ( )
halo_dunia("Azis")
halo_dunia("Bilal")
halo_dunia("Ridho")
halo_dunia("Imam")

# fungsi luas persegi panjang
def luas_persegi_panjang(panjang, lebar):
  print("P = ", panjang)
  print("L = ", lebar)
  rumus = panjang * lebar
  print("Hasil luas persegi panjang = ", rumus)

luas_persegi_panjang(10, 5)
luas_persegi_panjang(8, 100)
# def luas_segitiga(alas, tinggi):
  # 1/2 * alas * tinggi
