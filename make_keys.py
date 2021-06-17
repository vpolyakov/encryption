from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization

KEY_FILE_NAME = 'rsa_key'

private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048,
)

pr_pem = private_key.private_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PrivateFormat.TraditionalOpenSSL,
    encryption_algorithm=serialization.NoEncryption(),
)

with open(KEY_FILE_NAME, 'bw') as f:
    f.write(pr_pem)

public_key = private_key.public_key()
pub_pem = public_key.public_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PublicFormat.SubjectPublicKeyInfo,
)

with open(KEY_FILE_NAME + '.pub', 'bw') as f:
    f.write(pub_pem)
