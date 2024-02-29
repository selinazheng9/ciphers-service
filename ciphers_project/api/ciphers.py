def caesar_encode(plainText, shift):
    cipherText = ""
    for c in plainText:
        if (c.isupper()):
            result = chr((ord(c) + shift-65) % 26 + 65)
        else:
            result = chr((ord(c) + shift-97) % 26 + 97)
        cipherText += result
    return cipherText