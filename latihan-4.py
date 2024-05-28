def jumlah_rekursif(s):
    # Kasus dasar: jika string hanya memiliki satu karakter
    if len(s) == 1:
        return int(s)
    else:
        # Kasus rekursif: memecah karakter pertama dan menjumlahkannya dengan hasil rekursi dari sisa string
        return int(s[0]) + jumlah_rekursif(s[1:])

# Get input from the user
input = input("Masukkan String: ")

# Call the function with the user input
hasil = jumlah_rekursif(input)
print("Result:", hasil)