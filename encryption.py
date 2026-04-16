KEY = 12

def encrypt(message):
    return "".join(chr(ord(c) ^ KEY) for c in message)

def decrypt(message):
    return "".join(chr(ord(c) ^ KEY) for c in message)