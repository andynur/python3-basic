print("Python Beginner - Materi 5")
# # for loop (index di mulai dari 0 sampai seterusnya)
# # di balik layar range (1, 2, 3, 4, 5)
# for angka in range(1, 6):
#   print("Halo ke-", angka)
#   print("mantap ke-", angka)
# # dibawah ini gk masuk blok kode for karna diluar scope nya
# print("--- selesai ---") 
# # for loop pada string/text
# wifiJoglo = "hsijoglo"
# for huruf in wifiJoglo:
#   print(huruf, "-->")

# rentangNomor = range(1, 6)
# for no in rentangNomor:
#   print("*" * no)

# print("--- selesai lagi ---") 
# # while loop (selalu di jalankan sampai kondisi terpenuhi)
# # tekan ctrl+c kalau looping terus berjalan untuk mematikan proses
# num = 6
# while (num >= 1):
#   print("Jalan teros: ", num)
#   # num -= 2
#   num -= 1

# contoh flowchart cek umur
print("-- mulai --")
cekUmur = input("Berapa umur anda? ")
# seluruh input() dari user itu tipenya string
# konversi tipe nya jadi integer agar bisa di cek
angkaUmur = int(cekUmur)
print("Umur anda ", angkaUmur, " tahun")
if (angkaUmur >= 18):
  print("Boleh buat sim c")
else:
  print("Masih bocil FF, belum boleh yak!")

print("-- selesai --")π