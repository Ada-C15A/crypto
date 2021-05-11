def crypt_letter(letter, key_letter):
    return chr(ord(letter) ^ ord(key_letter))

def crypt(msg, key):
    key_len = len(key)
    return "".join([crypt_letter(letter, key[i % key_len]) for i, letter in enumerate(msg)])

def rot13(letter):
    if 'A' <= letter <= 'Z':
        offset = ord('A')
    elif 'a' <= letter <= 'z':
        offset = ord('a')
    else:
        return letter

    offset_letter = ord(letter) - offset + 13
    wrapped_letter = offset_letter % 26
    new_letter = chr(wrapped_letter + offset)

    return new_letter

def caesar(msg):
    return "".join([rot13(letter) for letter in msg])
    
def main():
    print(f"{caesar('Hello')=}")
    print(f"{crypt('Hello', 'key')=}")
    print(f"{caesar('Uryyb')=}")
    print(repr(crypt('#\x00\x15\x07\n', 'key')))

if __name__ == '__main__':
    main()
