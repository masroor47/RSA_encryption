def encrypt(e, N, message):
    ascii_values = []

    for i in message:
        ascii_values.append(pow (ord(i), e) % N)
    print(f"Length: {len(ascii_values)}")

    return ascii_values

# Encrypts each char as a sseparate int in an array
message_str = input("Enter the message: ")
e = int(input("Enter the encryption key: "))
N = int(input("Enter the N: "))

print(f"The encrypted message is: \n{encrypt(e, N, message_str)}")