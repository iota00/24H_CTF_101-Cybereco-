#!/usr/bin/python3
from secrets import token_bytes
from base64 import b64encode

# Modified RC4 implementation
# Original taken from https://jhafranco.com/2012/01/15/rc4-implementation-in-python-3/
state = [None] * 256
p = q = None
 
def setKey(key):
    """RC4 Key Scheduling Algorithm (KSA)"""
    global p, q, state
    state = [n for n in range(256)]
    p = q = j = 0
    for i in range(256):
        if len(key) > 0:
            j = (j + state[i] + key[i % len(key)]) % 256
        else:
            j = (j + state[i]) % 256
        state[i], state[j] = state[j], state[i]
 
def byteGenerator():
    """RC4 Pseudo-Random Generation Algorithm (PRGA)"""
    global p, q, state
    p = (p + 1) % 256
    q = (q + state[p]) % 256
    state[p], state[q] = state[q], state[p]
    return state[(state[p] + state[q]) % 256]

def byteGeneratorWrapper():
    """Prevent information leak (XOR with 0 will leak the encrypted character)"""
    b = byteGenerator()
    while b == 0:
        b = byteGenerator()
    return b
 
def encrypt(inputString):
    """Encrypt input string returning a byte list"""
    return [ord(p) ^ byteGeneratorWrapper() for p in inputString]
 
def decrypt(inputByteList):
    """Decrypt input byte list returning a string"""
    return "".join([chr(c ^ byteGeneratorWrapper()) for c in inputByteList])

# Load the flag
with open("./flag.txt", "r") as flagfile:
    flag = flagfile.read().rstrip("\n")

with open("output.txt", "w") as outfile:
    for _ in range(4096):
        # Generate random key
        key = token_bytes(200)
        setKey(key)
        # Encrypt flag
        outfile.write(b64encode(bytes(encrypt(flag))).decode() + "\n")
