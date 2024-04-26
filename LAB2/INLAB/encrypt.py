
plainText = input("Enter a one-word, lowercase message: ")

distance = int(input("Enter the distance value: "))

coded_message = ""

# Iterate through each character in the plaintext
for ch in plainText:
    # Convert character to its Unicode code point
    ord_value = ord(ch)
    
    # Calculate the cipher value by shifting the Unicode code point
    cipher_value = ord_value + distance

    # Check if the cipher value exceeds the Unicode code point for 'z'
    if cipher_value > ord('z'):
        # Wrap around if the cipher value exceeds 'z'
        cipher_value = ord('a') + (cipher_value - ord('z')) - 1

    # Append the coded character to the coded message
    coded_message += chr(cipher_value)

# Print the coded message
print(coded_message)



