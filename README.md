# Caesar Cipher in Python

This project implements a Caesar cipher in Python. The Caesar cipher is a simple encryption method that shifts each letter in a text by a certain number of positions in the alphabet. This program allows the user to either encrypt or decrypt a message using this method.

## Features

- **Encryption**: Shifts each letter in the text forward by a specified number of positions in the alphabet.
- **Decryption**: Shifts each letter in the text backward to retrieve the original text.
- Non-alphabetic characters (numbers, spaces, punctuation) remain unchanged.

## Code Structure

- `caesar_encrypt(text, shift)`: Function that encrypts the text by applying the specified shift.
- `caesar_decrypt(text, shift)`: Function that decrypts the text by applying a negative shift.
- `main()`: The main function that handles user interaction to choose between encryption and decryption, then performs the selected action.
