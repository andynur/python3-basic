print("MATERI 7 - PYTHON DATA STRUCTURE")
print("---------------------------------")
# Set -> { } -> tidak berurutan, berubah, tidak duplikat 
game_azka = {"valorant", "delta", "roblox"}
game_zaky = {"minecraft", "roblox", "point blank", "cod"}
game_azka.add('minecraft')
game_zaky.add('roblox')
game_azka.remove('valorant')

print("Game Azka: ", game_azka)
print("Game Zaky: ", game_zaky)
game_gabungan = game_azka | game_zaky # | -> (or) atau
print("Daftar Game: ", game_gabungan)
# for (loop) untuk mengeluarkan isi item dari Set
for game in game_gabungan:
  print('->', game)
  print('--> Transfer data game', game, ' ke PS5')
 
print("-------------- dict ------------------")
# Dictionary (dict) -> {key:value} / {kunci:isi}
# -> berurutan, berubah, tidak duplikat
kamus_anime = {
  "blue_lock": "Isagi Ren",
  "demon_slayer": "Tanjiro",
  "waifu": {
    "one_piece": "big mom",
    "demon_slayer": "nezuko",
  }
}
print("Kamus Anime:", kamus_anime)
print("MC demon slayer:", kamus_anime["demon_slayer"])
print("Waifu one piece:", kamus_anime["waifu"]["one_piece"])
# nambah item baru ke dictionary
kamus_anime["naruto"] = "Shikamaru"
print("MC naruto:", kamus_anime["naruto"])
# mengubah item dari dictionary
kamus_anime["demon_slayer"] = "Zenitsu"
# menghapus item dari dictionary
del(kamus_anime['blue_lock'])
print("Kamus Anime Terbaru:", kamus_anime)