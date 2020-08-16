def decrypt(d, N, ascii_values):
    message = ""
    for i in range(len(ascii_values)):
        ascii_values[i] = pow (ascii_values[i], d, N)

    print(ascii_values)
    for i in ascii_values:
        message += chr(i)
    return message

# Decrypts each value as an individual char
ascii_values = []
value = int(input("Enter value: "))
while value != -1:
    ascii_values.append(value)
    value = int(input("Enter value: "))

print("You entered: " + ascii_values)

d = int(input("Enter the private key: "))
N = int(input("Enter the N: "))

print(f"The decrypted message is: {decrypt(d, N, ascii_values)}")