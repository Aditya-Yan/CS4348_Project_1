import sys

passkey = None


def vigenere_encrypt(text, key):
    result = ""
    key_index = 0

    for char in text:
        shift = ord(key[key_index % len(key)]) - ord('A')
        encrypted = chr(((ord(char) - ord('A') + shift) % 26) + ord('A'))
        result += encrypted
        key_index += 1

    return result

def vigenere_decrypt(text, key):
    result = ""
    key_index = 0

    for char in text:
        shift = ord(key[key_index % len(key)]) - ord('A')
        decrypted = chr(((ord(char) - ord('A') - shift) % 26) + ord('A'))
        result += decrypted
        key_index += 1

    return result

for line in sys.stdin:
    command_line = line.strip()

    if not command_line:
        continue

    parts = command_line.split(" ", 1)
    command = parts[0]
    argument = parts[1] if len(parts) > 1 else ""

    if command == "PASS":
        passkey = argument
        print("RESULT")
        sys.stdout.flush()

    elif command == "ENCRYPT":
        if passkey is None:
            print("ERROR Password not set")
        else:
            encrypted = vigenere_encrypt(argument, passkey)
            print(f"RESULT {encrypted}")

        sys.stdout.flush()
    
    elif command == "DECRYPT":
        if passkey is None:
            print("ERROR Password not set")
        else:
            decrypted = vigenere_decrypt(argument, passkey)
            print(f"RESULT {decrypted}")
        sys.stdout.flush()

    elif command == "QUIT":
        break