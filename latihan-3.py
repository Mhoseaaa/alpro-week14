def hitung_ganjil(n):
    if n == 1:
        return 1
    else:
        return (2 * n - 1) + hitung_ganjil(n-1)
    
# Test cases
print(hitung_ganjil(1))  # Expected output: 1
print(hitung_ganjil(2))  # Expected output: 4
print(hitung_ganjil(3))  # Expected output: 9
print(hitung_ganjil(4))  # Expected output: 16
print(hitung_ganjil(5))  # Expected output: 25