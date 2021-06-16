from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import padding

with open('rsa_key.pub', 'rb') as public_key_file:
    public_key_file_content = public_key_file.read()

public_key = serialization.load_pem_public_key(public_key_file_content)

with open('plaintext', 'rb') as message_file:
    message = message_file.read()

ciphertext = public_key.encrypt(
    message,
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

with open('ciphertext', 'bw') as cipher_file:
    cipher_file.write(ciphertext)
