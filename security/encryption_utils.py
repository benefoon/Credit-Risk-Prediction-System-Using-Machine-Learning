from cryptography.fernet import Fernet

# Generate and store this securely
key = Fernet.generate_key()
cipher = Fernet(key)

def encrypt_data(data):
    """Encrypts data before storing"""
    return cipher.encrypt(data.encode()).decode()

def decrypt_data(encrypted_data):
    """Decrypts stored encrypted data"""
    return cipher.decrypt(encrypted_data.encode()).decode()

# Example Usage
encrypted_credit_score = encrypt_data("750")
decrypted_credit_score = decrypt_data(encrypted_credit_score)

print(f"Encrypted: {encrypted_credit_score}")
print(f"Decrypted: {decrypted_credit_score}")
