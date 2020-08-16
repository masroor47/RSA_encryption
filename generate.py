# Finding the Greatest Common Denominator
def gcd(p, q):
    while q != 0:
        p, q = q, p%q
    return p

# Checking if the two numbers are coprime
def is_coprime(x, y):
    return gcd(x, y) == 1

# Extended gcd
def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)
        
# Modular inverse
def modinv(e, f):
    g, x, y = egcd(e, f)
    return x % f

# Generating e and d keys using the two provided prime numbers
def generate_keys(p, q):
    N = p * q

    # Finding phi. How many coprimes with N
    f = (p - 1) * (q - 1) 

    # 65537 is the commonly used value for e
    e = 65537
        
    # Finding d
    d = modinv(e, f)

    return N, e, d

print("Welcome to the RSA key generator!")

p = int(input("First prime number: "))
q = int(input("Second prime number: "))

N, e, d = generate_keys(p, q)
print(f"N = {N}\ne = {e}\nd = {d}")
