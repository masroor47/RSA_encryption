def encrypt(e, N, message):
    ascii_values = []
    
    # Placing the ASCII values of the string characters in an Int array
    for i in message:
        ascii_values.append(ord(i))

    print(ascii_values)

    # Replacing each value with the encrypted version of itself
    for i in range(len(ascii_values)):
        ascii_values[i] = pow (ascii_values[i], e) % N
        
    return ascii_values

message_str = input("Enter the message: ")
e = int(input("Enter the encryption key: "))
N = int(input("Enter the N: "))

print(f"The encrypted message is: {encrypt(e, N, message_str)}")