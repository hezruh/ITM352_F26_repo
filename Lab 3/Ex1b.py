# Exercise 1b: Fernet Encryption
# Name: Hezra Calventas
# Date: 9/9/2026

from cryptography.fernet import Fernet

key = Fernet.generate_key()
cipherSuite = Fernet(key)

encodedText = cipherSuite.encrypt(b"Hello, World!")
print("Encoded Text:", encodedText)
decodedText = cipherSuite.decrypt(encodedText)
print("Decoded Text:", decodedText)