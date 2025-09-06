print("Materi 9C - Python Function")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
# def -> fungsi lebih dari 1 baris
def halo_dek(nama):
  # f (format string) gunakan {} untuk variable
  print(f"Halo dek {nama}")
  print(f"Apa kabar dek {nama}")
  print("---------")
# lambda -> fungsi anonim yang 1 baris saja
halo_kak = lambda nama: print(f"Halo kak {nama}")
#fungsi tidak akan berguna jika tidak dipanggil
halo_dek("Nezuko")
halo_dek("Anya")
halo_kak("Jhonson")
halo_kak("Tegar")
print("---------")
# higher order function (map, sorted, filter)
uang_jajan = [100000,200000,10000,50000,75000]
# map() -> mentransformasi data item
kurangi_jajan = map(lambda uang: uang - 5000, uang_jajan)
list_kurangi_jajan = list(kurangi_jajan)
print(f"Uang jajan: {uang_jajan}")
print(f"Kurangin jajan: {list_kurangi_jajan}")
# sorted() -> mengurutkan data
urutkan_uang = sorted(uang_jajan)
balik_uang = sorted(uang_jajan, reverse=True)
print(f"Urutkan uang: {urutkan_uang}")
print(f"Urutkan uang terbalik: {balik_uang}")
# filter() -> menyaring data sesuai kondisi
filter_uang_gede = filter(lambda uang: uang > 50000, uang_jajan)
list_uang_gede = list(filter_uang_gede)
print(f"Filter uang gede: {list_uang_gede}")