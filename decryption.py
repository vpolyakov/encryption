from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import padding

with open('rsa_key', 'rb') as key_file:
    key_file_content = key_file.read()

private_key = serialization.load_pem_private_key(
    key_file_content,
    password=None,
)

with open('ciphertext', 'rb') as cipher_file:
    ciphertext = cipher_file.read()

encoded_plaintext = private_key.decrypt(
    ciphertext,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
<<<<<<< HEAD
        label=None,
    ),
=======
        label=None
    )
>>>>>>> refs/remotes/origin/master
)

print(encoded_plaintext.decode())
