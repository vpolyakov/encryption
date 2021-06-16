from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import serialization

with open('rsa_key', 'rb') as key_file:
    content_key_file = key_file.read()

private_key = serialization.load_pem_private_key(
    content_key_file,
    password=None,
)

with open('message', 'rb') as message_file:
    message = message_file.read()

signature = private_key.sign(
    message,
    padding.PSS(
        mgf=padding.MGF1(hashes.SHA256()),
        salt_length=padding.PSS.MAX_LENGTH,
    ),
    hashes.SHA256(),
)

with open('sign', 'bw') as sign_file:
    sign_file.write(signature)
