print("---- MATERI 5 ----")
jumlahRentang = 4
# item (variabel baru) adalah index
# range(jumlahRentang) adalah target nya
for item in range(jumlahRentang):
  print("Halo Lur: ", item)

# huruf (variabel baru) adalah index
# kataKu adalah target nya
kataKu = "Coding"
for huruf in kataKu:
  print(huruf)

# perulangan while (sampai kondisi terpenuhi / true)
# selama input dari variabel jawab
# diisikan 'ya' maka ulangi terus
jawab = 'ya'
hitung = 0
while(jawab == 'ya'):
  jawab = input("Ulang lagi tidak? ")
  hitung += 1
print("program di ulangi sebanyak: ", hitung)

# simulasi flowchart uji sim
print("--- mulai ---")
tanyaUmur = input("Berapa umur mu? ")
# konversi string ke integer
angkaUmur = int(tanyaUmur) 
print("Umur mu: ", angkaUmur, " tahun")
if (angkaUmur >= 18):
  print("Boleh membuat sim")
else:
  print("Tidak boleh membuat sim")
print("--- selesai ---")