def caesar_encode(plainText, shift):
    cipherText = ""
    for c in plainText:
        c_encoded = ord(c) + shift
        c_encoded = chr(c_encoded)
        cipherText += c_encoded
    return cipherText