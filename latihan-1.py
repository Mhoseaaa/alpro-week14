def cek_prima(n, i=2):
    # Base cases
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % i == 0:
        return False
    if i * i > n:
        return True
    
    # Recursive case
    return cek_prima(n, i + 1)

# user input
n = int(input("Enter a number: "))

# Call the function
prima = cek_prima(n)
print(f"{n} merupakan prima? : {prima}")
