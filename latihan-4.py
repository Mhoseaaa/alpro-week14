def jumlah_rekursif(s):
    # Kasus dasar: jika string hanya memiliki satu karakter
    if len(s) == 1:
        return int(s)
    else:
        # Kasus rekursif: memecah karakter pertama dan menjumlahkannya dengan hasil rekursi dari sisa string
        return int(s[0]) + jumlah_rekursif(s[1:])

# input user
input = input("Masukkan String: ")

# Panggil fungsi jumlah_rekursif
hasil = jumlah_rekursif(input)
print("Result:", hasil)