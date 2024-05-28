def hitung_ganjil(n):
    if n == 1:
        return 1
    else:
        return (2 * n - 1) + hitung_ganjil(n-1)