print("Python Beginner - Materi 5")
# for loop (index di mulai dari 0 sampai 5)
for angka in range(0, 5):
  print("Halo ke-", angka)
  print("mantap!")
print("--- selesai ---") # ini gk masuk loop karna diluar blok kode
# for loop ke string
sandiWifi = "hsijoglo"
for huruf in sandiWifi:
  print(huruf, " ==> ")
# while loop (ulangi sampai kondisi terpenuhi)
no = 1
batas = 10
while (no < batas):
  # print("ulangi ke-", no)
  print("*" * no)
  no += 1
# kalau looping berjalan terus, tekan ctrl+c 
# untuk membatalkan eksekusi program

# simulasi flowchart cek umur sim
print(" -- mulai --")
cekUmur = input("Berapa umur anda? ")
# konversi / mengganti tipe data suatu variabel
# fungsi int() mengganti string ke integer
angkaUmur = int(cekUmur)
if (angkaUmur >= 18):
  print("Boleh buat sim baru")
else:
  print("Masih bocil, belum boleh")

print(" -- selesai --")