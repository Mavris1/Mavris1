import base64
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

UserPassword = input("If you have followed my instructions, this is where you add it..: ")
password = UserPassword.encode()

mysalt = b'J>\xbav\xc5\xa6\xa01Sg\xa7\xb3,\xc3\xa3\x02'

kdf = PBKDF2HMAC (
    algorithm=hashes.SHA256,
    length=32,
    salt=mysalt,
    iterations=100000,
    backend=default_backend()

)

key = base64.urlsafe_b64encode(kdf.derive(password))

print(key.decode())
