#include <iostream>
#include <string>

int main() {
    std::string plainText;
    std::cout << "Enter a one-word, lowercase message: ";
    std::cin >> plainText;

    int distance;
    std::cout << "Enter the distance value: ";
    std::cin >> distance;

    std::string code = "";

    for (char ch : plainText) {
        int ordValue = static_cast<int>(ch);
        int cipherValue = ordValue + distance;

        if (cipherValue > static_cast<int>('z')) {
            cipherValue = static_cast<int>('a') + (cipherValue - static_cast<int>('z')) - 1;
        }

        code += static_cast<char>(cipherValue);
    }

    std::cout << "Encoded message: " << code << std::endl;

    return 0;
}