def caesar_encrypt(text, shift):
    result = ""
    shift_amount = shift % 26  # Gérer les décalages supérieurs à 26 ainsi que les décalages négatifs

    for char in text:
        if char.isalpha():  # Vérifier si le caractère est une lettre
            start = ord('a') if char.islower() else ord('A')

            # Calcul du caractère chiffré
            new_char = chr((ord(char) - start + shift_amount) % 26 + start)
            result += new_char
        else:
            result += char  # Les caractères non alphabétiques restent inchangés

    return result


def caesar_decrypt(text, shift):
    # Appeler la fonction de chiffrement avec un décalage négatif pour déchiffrer
    return caesar_encrypt(text, -shift)


def main():
    action = input("Would you like to encrypt or decrypt your message? (e/d): ").lower()
    if action not in ['e', 'd']:
        print("Invalid choice! Please enter 'e' for encrypting or 'd' for decrypting.")
        return

    message = input("Enter the message: ")
    shift = int(input("Enter the shift value: "))

    if action == 'e':
        encrypted_message = caesar_encrypt(message, shift)
        print(f"Encrypted message: {encrypted_message}")
    else:
        decrypted_message = caesar_decrypt(message, shift)
        print(f"Decrypted message: {decrypted_message}")

if __name__ == "__main__":
    main()
    
    
    
    
    
    
    