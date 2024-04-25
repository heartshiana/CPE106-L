# CPE106 - L 
# Heart Ursua, Jhianne Sarmiento, Larrline Quiambao, Syrah Olaso, Hannah Angeles

coded_text = input("Enter a one-word, lowercase message: ")
distance_value = int(input("Enter the distance value: "))

# Initialize an empty string to store the decoded message
decoded_text = ""

for character in coded_text:
    # Convert the character to its ASCII code
    char_code = ord(character)
    
    # Decode the character by subtracting the distance value
    decoded_char_code = char_code - distance_value

    # Wrap around if the decoded character code is out of range for lowercase letters
    if decoded_char_code < ord('a'):
        decoded_char_code = ord('z') - (distance_value - (char_code - ord('a')) - 1)

    # Append the decoded character to the decoded message
    decoded_text += chr(decoded_char_code)

print(decoded_text)


