from cryptography.fernet import Fernet

key = b'577xr4A2lKSrJ5ET9q7GB6ehR8g20MY-Eisdvrtxp_w='

fernet = Fernet(key)

def encrypt(value):
    return fernet.encrypt(value.encode()).decode()

def decrypt(value):
    return fernet.decrypt(value.encode()).decode()