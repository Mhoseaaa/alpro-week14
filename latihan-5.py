def kombinasi(n, r):
    if r == 0 or r == n:
        return 1
    else:
        return kombinasi(n-1, r-1) + kombinasi(n-1, r)

n = int(input("Masukkan nilai n: "))
r = int(input("Masukkan nilai r: "))

hasil = kombinasi(n, r)
print("Hasil kombinasi dari C(", n, ",", r, ") adalah", hasil)