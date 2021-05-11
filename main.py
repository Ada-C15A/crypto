from caesar import caesar

def crypt_letter(letter, key_letter):
    return chr(ord(letter) ^ ord(key_letter))

def crypt(msg, key):
    key_len = len(key)
    return "".join([crypt_letter(letter, key[i % key_len]) for i, letter in enumerate(msg)])

    
def main():
    print(f"{caesar('Hello')=}")
    print(f"{crypt('Hello', 'key')=}")
    print(f"{caesar('Uryyb')=}")
    print(repr(crypt('#\x00\x15\x07\n', 'key')))

if __name__ == '__main__':
    main()
