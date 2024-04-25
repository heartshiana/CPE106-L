
// CPE106 - L 
// Heart Ursua, Jhianne Sarmiento, Larrline Quiambao, Syrah Olaso, Hannah Angeles

#include <iostream>
#include <string>

using namespace std;

int main() {
    string coded_text;
    cout << "Enter a one-word, lowercase message: ";
    cin >> coded_text;

    // Input the distance value
    int distance_value;
    cout << "Enter the distance value: ";
    cin >> distance_value;

    // Initialize an empty string to store the decoded message
    string decoded_text = "";

    // Iterate over each character in the coded message
    for (char character : coded_text) {
        // Convert the character to its ASCII code
        int char_code = static_cast<int>(character);

        // Decode the character by subtracting the distance value
        int decoded_char_code = char_code - distance_value;

        // Wrap around if the decoded character code is out of range for lowercase letters
        if (decoded_char_code < static_cast<int>('a')) {
            decoded_char_code = static_cast<int>('z') - (distance_value - (char_code - static_cast<int>('a')) - 1);
        }

        // Append the decoded character to the decoded message
        decoded_text += static_cast<char>(decoded_char_code);
    }

    // Output the decoded message
    cout << "Decoded message: " << decoded_text << endl;

    return 0;
}
