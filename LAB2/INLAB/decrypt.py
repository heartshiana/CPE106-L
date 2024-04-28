codedText = input("Enter the coded text: ")
distance = int(input("Enter the distance value: "))

# Initialize an empty string for the plaintext
text = ''

# Iterate through each character in the coded text
for ch in codedText:
    if ch.isalpha():  # Check if the character is a letter
        ord_value = ord(ch)
        cipher_value = ord_value - distance

        # Check if the letter is lowercase
        if ch.islower():
            if cipher_value < ord('a'):
                cipher_value = ord('z') - (distance - (ord_value - ord('a')) - 1)
        # Check if the letter is uppercase
        elif ch.isupper():
            if cipher_value < ord('A'):
                cipher_value = ord('Z') - (distance - (ord_value - ord('A')) - 1)

        # Append the decrypted character to the plaintext
        text += chr(cipher_value)
    else:
        # Non-alphabetic characters are added as is
        text += ch

# Print the decrypted plaintext
print(text)

