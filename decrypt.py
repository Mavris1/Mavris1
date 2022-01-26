import sys
from sys import argv
import cryptography
from cryptography.fernet import Fernet

key = input('Please input the decryption key:')
cipher = Fernet(key)

with open('encrypted_Mavris2', 'rb') as df:
    encrypted_data = df.read()

decrypted_file = cipher.decrypt(encrypted_data)

with open('decrypted_12kMP.txt', 'wb') as df:
    df.write(decrypted_file)

x1 = input('Would you like to see the list of contents in your decrypted file?')

if(x1 == 'yes' or 'Y' or 'Yes' or 'Yeah' or 'y' or 'yeah'):
    f = open('decrypted_Mavris2.txt', 'r')
    file_contents = f.read()
    print(file_contents)
    f.close()
else:
    print('Good job.')
