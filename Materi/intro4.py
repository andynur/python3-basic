nama = input("Masukkan nama lengkap: ")
umur = int(input("Masukkan umur: "))
kelas = input("Masukkan kelas: ")
hobi = input("Apa hobi favoritmu? ")
cita2 = input("Apa cita-citamu di masa depan? ")
waktu_belajar = input("Kamu lebih suka belajar di pagi atau malam? ")
print("Pilih salah satu (1-5):")
print("1. Wibu\n2. Gamer\n3. K-Popers\n4. Anak konten\n5. Anak nongki")
tipe = int(input("Kamu lebih merasa sebagai: "))

tahun_lahir = 2025 - umur

print("\n===== PROFIL DIGITAL SAYA =====")
print(f"Halo! Nama saya {nama}.")
print(f"Saya berusia {umur} tahun dan sekarang duduk di kelas {kelas}.")
print(f"Hobi saya adalah {hobi}, dan saya bercita-cita menjadi {cita2}.")
print(f"Saya lebih suka belajar di {waktu_belajar} hari.")
print(f"\nSaya diperkirakan lahir pada tahun {tahun_lahir}.")

print("\n=== KEPRIBADIAN DIGITAL ===")
if tipe == 1:
    print("Kamu memilih: Wibu")
    print("Wah, ada aroma bawang yang menyeruak di sini... T__T")
elif tipe == 2:
    print("Kamu memilih: Gamer")
    print("Kamu pasti jago multitasking: nembak musuh sambil ngerjain tugas! 🎮📚")
elif tipe == 3:
    print("Kamu memilih: K-Popers")
    print("ARMY? BLINK? Musik bikin kamu semangat ngoding ya? 🎶💻")
elif tipe == 4:
    print("Kamu memilih: Anak Konten")
    print("TikTok dulu baru tugas? Jangan lupa jadi content creator yang edukatif ya!")
elif tipe == 5:
    print("Kamu memilih: Anak Nongki")
    print("Sibuk jalan-jalan? Semoga tetap sempat ngoding walau sambil ngopi! ☕🚶")
else:
    print("Pilihan tidak dikenal. Kamu unik banget sih 😁")

print("================================")
