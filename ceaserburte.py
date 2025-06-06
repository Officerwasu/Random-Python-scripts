def caesar_bruteforce(ciphertext):
    print(f"\nAttempting to brute-force: '{ciphertext}'\n")
    for key in range(1, 26):
        decrypted_message = ""
        for char in ciphertext:
            if 'a' <= char <= 'z':
                decrypted_char_code = ord(char) - key
                if decrypted_char_code < ord('a'):
                    decrypted_char_code += 26
                decrypted_message += chr(decrypted_char_code)
            elif 'A' <= char <= 'Z':
                decrypted_char_code = ord(char) - key
                if decrypted_char_code < ord('A'):
                    decrypted_char_code += 26
                decrypted_message += chr(decrypted_char_code)
            else:
                decrypted_message += char
        print(f"Shift -{key:2}: {decrypted_message}")


user_ciphertext = input("Enter ciphertext to brute-force: ")
caesar_bruteforce(user_ciphertext)