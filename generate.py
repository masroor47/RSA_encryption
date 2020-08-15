# Finding the Greatest Common Denominator
def gcd(p, q):
    while q != 0:
        p, q = q, p%q
    return p

# Checking if the two numbers are coprime
def is_coprime(x, y):
    return gcd(x, y) == 1

# Generating e and d keys using the two provided prime numbers
def generate_keys(p, q):
    N = p * q

    # Finding phi. How many coprimes with N
    f = (p - 1) * (q - 1) 

    # Finding e
    for i in range(2, f):
        if is_coprime(i, N) and is_coprime(i, f):
            e = i
            break
        
    # Finding d
    d = 1
    while True:
        if d * e % f == 1:
            break
        d += 1


    return N, e, d

print("Welcome to the RSA key generator!")

p = int(input("First prime number: "))
q = int(input("Second prime number: "))

N, e, d = generate_keys(p, q)
print(f"N = {N}\ne = {e}\nd = {d}")
