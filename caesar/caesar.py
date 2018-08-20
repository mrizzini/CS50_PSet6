import sys
from cs50 import get_string

if len(sys.argv) != 2:
    print("ERROR: User must type in just two command-line arguements, with the second being a non-negative integer")
    sys.exit(1)

key = int(sys.argv[1])

plainText = get_string("Plaintext: ")
print("ciphertext: ", end="")

for i in range(len(plainText)):
    if not plainText[i].isalpha():
        print(plainText[i], end="")
    if plainText[i].isupper():
        upperASCII = (ord(plainText[i]) - 65)
        upperConvert = (upperASCII + key) % 26
        upperCipher = chr(upperConvert + 65)
        print(upperCipher, end="")
    if plainText[i].islower():
        lowerASCII = (ord(plainText[i]) - 97)
        lowerConvert = (lowerASCII + key) % 26
        lowerCipher = chr(lowerConvert + 97)
        print(lowerCipher, end="")
print()