print("Hello world!")
x = 10 * 5
y = 20 + 20
# operator += (y = y + 10)
y += 10
# operator -= (y = y - 5)
y -= 5
print(x, y)
# input() berguna menerima inputan dari user
nilaiUmur = input("Berapa umur mu? ")
print("Umur kamu", nilaiUmur, " tahun")

# if - else statement
# if (jika terpenuhi) - else (selainnya atau tidak terpenuhi)
# operator pembanding == != > <
if (nilaiUmur == "25"):
  print("Umur nya ketuaan bang")
elif (nilaiUmur == "10"): # nilai umur adalah 10
  print("Umur nya kemudaan dek")
else:
  print("Umur nya cukup aja")

# operator != (tidak sama dengan)
# kelasBudi = "A"
kelasBudi = input("Budi kelas berapa? ")
statusKelasBudi = kelasBudi != "C" # True
print("statusKelasBudi: ", statusKelasBudi)

statusKehadiran = "hadir"
if (statusKehadiran != "alpha"): # tidak sama dengan alpha
  print("mendapatkan point +1")
else: # statusnya alpha
  print("mendapatkan point -1")

# operator > (lebih besar) dan < (lebih kecil)
# sistem peringkat A (90 - 100), B (80 - 89), C (70 - 79), D (selainnya)
nilaiUjian = 40
print("nila ujian:", nilaiUjian)
if (nilaiUjian > 89 and nilaiUjian < 101):
  print("Kamu peringkat A")
elif (nilaiUjian > 79 and nilaiUjian < 90):
  print("Kamu peringkat B")
else:
  print("Kamu peringkat D")