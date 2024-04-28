# CPE106 - L 
# Heart Ursua, Jhianne Sarmiento, Larrline Quiambao, Syrah Olaso, Hannah Angeles

coded_text = input("Enter the coded text: ")
distance_value = int(input("Enter the distance value: "))
decoded_text = ''

for character in coded_text:
    if character.isalpha():  # Check if the character is a letter
        char_code = ord(character)
        decoded_char_code = char_code - distance_value

        if character.islower():  # Check if the letter is lowercase
            if decoded_char_code < ord('a'):
                decoded_char_code = ord('z') - (distance_value - (char_code - ord('a')) - 1)
        elif character.isupper():  # Check if the letter is uppercase
            if decoded_char_code < ord('A'):
                decoded_char_code = ord('Z') - (distance_value - (char_code - ord('A')) - 1)

        decoded_text += chr(decoded_char_code)
    else:
        decoded_text += character  # Non-alphabetic characters are added as is

print(decoded_text)



