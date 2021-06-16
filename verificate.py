from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import padding

with open('rsa_key.pub', 'rb') as public_key_file:
    public_key_file_content = public_key_file.read()

public_key = serialization.load_pem_public_key(public_key_file_content)

with open('message', 'rb') as message_file:
    message = message_file.read()

with open('sign', 'rb') as sign_file:
    signature = sign_file.read()

public_key.verify(
    signature,
    message,
    padding.PSS(
        mgf=padding.MGF1(hashes.SHA256()),
        salt_length=padding.PSS.MAX_LENGTH
    ),
    hashes.SHA256()
)
