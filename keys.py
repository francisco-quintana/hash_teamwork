import Crypto
import binascii

from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

random_generator = Crypto.Random.new().read

    #esto nos genera un objeto rsa y la llave privada
private_key = RSA.generate(1024, random_generator)

    #se crea la llave publica basandose de la privada
public_key = private_key.publickey()

    #convierte el objeto rsa en bytes
private_key=private_key.exportKey(format='DER')
public_key=public_key.exportKey(format='DER')

    #convierte bytes a utf-8 o a una llave mas legible
private_key = binascii.hexlify(private_key).decode('utf-8')
public_key = binascii.hexlify(public_key).decode('utf-8')