def decrypt(d, N, enc_message):
    return pow(enc_message, d) % N

to_decrypt = int(input("What do you want to decrypt: "))
d = int(input("Enter the private key: "))
N = int(input("Enter the N: "))

print(f"The decrypted message is: {decrypt(d, N, to_decrypt)}")