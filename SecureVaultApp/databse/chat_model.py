from db_setup import chats_collection
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import base64
from datetime import datetime

# Generate RSA keys for encryption/decryption
def generate_rsa_keys():
    """Generate RSA key pair for secure communication."""
    key = RSA.generate(2048)
    private_key = key.export_key()
    public_key = key.publickey().export_key()
    return private_key, public_key

private_key, public_key = generate_rsa_keys()

def encrypt_message(message, recipient_public_key):
    """Encrypt message with recipient's RSA public key."""
    recipient_key = RSA.import_key(recipient_public_key)
    cipher = PKCS1_OAEP.new(recipient_key)
    encrypted_message = cipher.encrypt(message.encode())
    return base64.b64encode(encrypted_message).decode()

def store_chat(sender, receiver, message):
    """Encrypt and store chat message securely."""
    encrypted_msg = encrypt_message(message, public_key)
    chat_data = {
        "sender": sender,
        "receiver": receiver,
        "encrypted_message": encrypted_msg,
        "timestamp": datetime.utcnow()
    }
    chats_collection.insert_one(chat_data)
    print(f"Encrypted message from {sender} to {receiver} stored successfully!")

# Example usage
if __name__ == "__main__":
    store_chat("john_doe", "jane_smith", "Hello, this is a private message!")
