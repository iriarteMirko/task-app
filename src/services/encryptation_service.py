from cryptography.fernet import Fernet

class EncryptionService:
    def __init__(self, key_path='secret.key'):
        self.key = self.load_or_generate_key(key_path)
        self.cipher_suite = Fernet(self.key)
    
    def load_or_generate_key(self, key_path: str) -> bytes:
        try:
            with open(key_path, 'rb') as key_file:
                return key_file.read()
        except FileNotFoundError:
            key = Fernet.generate_key()
            with open(key_path, 'wb') as key_file:
                key_file.write(key)
            return key
    
    def encrypt(self, data: str) -> str:
        try:
            return self.cipher_suite.encrypt(data.encode()).decode()
        except Exception:
            raise ValueError('Error al encriptar los datos')
    
    def decrypt(self, encrypted_data: str) -> str:
        try:
            return self.cipher_suite.decrypt(encrypted_data.encode()).decode()
        except Exception:
            raise ValueError('Error al desencriptar los datos')