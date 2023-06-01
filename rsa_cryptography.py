import random

def generate_keypair(p, q):
    n = p * q
    phi = (p - 1) * (q - 1)

    # Find e such that 1 < e < phi and gcd(e, phi) = 1
    e = random.randrange(1, phi)
    while gcd(e, phi) != 1:
        e = random.randrange(1, phi)

    # Find d such that d*e ≡ 1 (mod phi)
    d = mod_inverse(e, phi)
    
    return ((e, n), (d, n))

def encrypt(public_key, plaintext):
    e, n = public_key
    cipher = [pow(ord(char), e, n) for char in plaintext]
    return cipher

def decrypt(private_key, ciphertext):
    d, n = private_key
    plaintext = [chr(pow(char, d, n)) for char in ciphertext]
    return ''.join(plaintext)

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def mod_inverse(a, m):
    if gcd(a, m) != 1:
        return None
    _, x, _ = extended_gcd(a, m)
    return x % m

def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = extended_gcd(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd, x, y

# Example usage
p = 61
q = 53
public_key, private_key = generate_keypair(p, q)

plaintext = "Hello, World!"
print("Plaintext:", plaintext)

ciphertext = encrypt(public_key, plaintext)
print("Ciphertext:", ciphertext)

decrypted_text = decrypt(private_key, ciphertext)
print("Decrypted text:", decrypted_text)
