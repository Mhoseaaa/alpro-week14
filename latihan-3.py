def hitung_ganjil(n):
    if n == 1:
        return 1
    else:
        return (2 * n - 1) + hitung_ganjil(n-1)

n = int(input("Masukkan angka: "))
hasil = hitung_ganjil(n)
print("Hasil penjumlahan bilangan ganjil dari 1 hingga", n, "adalah", hasil)