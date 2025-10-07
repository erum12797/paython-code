def atbash(text):
    result = ""
    for ch in text:
        if ch.isupper():
            result += chr(90 - (ord(ch) - 65))
        elif ch.islower():
            result += chr(122 - (ord(ch) - 97))
        else:
            result += ch
    return result  

if __name__ == "__main__": 
    msg = input("Enter text: ")
    encryption = atbash(msg)
    decryption = atbash(encryption)

    print("Encryption:", encryption)
    print("Decryption:", decryption)


