def cek_palindrom(kata):
    # Basis: jika panjang kalimat <= 1, maka kalimat tersebut adalah palindrom
    if len(kata) <= 1:
        return True
    
    # Rekursi: bandingkan karakter pertama dan terakhir kalimat
    if kata[0] == kata[-1]:
        # Panggil fungsi cek_palindrome dengan menghilangkan karakter pertama dan terakhir kalimat
        return cek_palindrom(kata[1:-1])
    else:
        return False

# Contoh penggunaan
kalimat = input("Masukkan kalimat: ")
if cek_palindrom(kalimat):
    print("Kalimat adalah palindrom")
else:
    print("Kalimat bukan palindrom")
