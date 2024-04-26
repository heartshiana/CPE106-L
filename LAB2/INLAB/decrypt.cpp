#include <iostream>
#include <string>

int main() {
    std::string code;
    std::cout << "Enter the coded text: ";
    std::cin >> code;

    int distance;
    std::cout << "Enter the distance value: ";
    std::cin >> distance;

    std::string plainText = "";

    for (char ch : code) {
        int ordValue = static_cast<int>(ch);
        int cipherValue = ordValue - distance;

        if (cipherValue < static_cast<int>('a')) {
            cipherValue = static_cast<int>('z') - (distance - (ordValue - static_cast<int>('a')) - 1);
        }

        plainText += static_cast<char>(cipherValue);
    }

    std::cout << "Decoded message: " << plainText << std::endl;

    return 0;
}
