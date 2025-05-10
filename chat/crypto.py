from cryptography.fernet import Fernet
from config import settings

print(Fernet.generate_key().decode())

fernet = Fernet(settings.FERNET_KEY.encode())
def encrypt_message(message: str) -> str:
    return fernet.encrypt(message.encode()).decode()

def decrypt_message(encrypted_message: str) -> str:
    return fernet.decrypt(encrypted_message.encode()).decode()