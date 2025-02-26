from db_setup import files_collection
from Crypto.Cipher import AES
import base64
import os
from datetime import datetime

# Generate a random 16-byte AES key (In production, store securely)
AES_KEY = os.urandom(16)

def encrypt_file(data):
    """Encrypt file data before storing using AES."""
    cipher = AES.new(AES_KEY, AES.MODE_EAX)
    ciphertext, tag = cipher.encrypt_and_digest(data.encode())
    return base64.b64encode(cipher.nonce + tag + ciphertext).decode()

def store_file(file_name, file_content, owner, access_level):
    """Save an encrypted file to MongoDB."""
    encrypted_data = encrypt_file(file_content)
    file_data = {
        "file_name": file_name,
        "encrypted_data": encrypted_data,
        "owner": owner,
        "access_level": access_level,  # Access control level
        "uploaded_at": datetime.utcnow()
    }
    files_collection.insert_one(file_data)
    print(f"File '{file_name}' stored successfully!")

# Example usage
if __name__ == "__main__":
    store_file("confidential.txt", "This is a secure file.", "john_doe", "Manager")
