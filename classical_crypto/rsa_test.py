import time
from cryptography.hazmat.primitives.asymmetric import rsa

def rsa_benchmark():
    start = time.time()

    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048
    )

    end = time.time()

    execution_time = end - start

    public_key = private_key.public_key()

    private_size = private_key.key_size
    public_size = public_key.key_size

    return {
        "Algorithm": "RSA-2048",
        "KeyGen_Time": execution_time,
        "Private_Key_Size": private_size,
        "Public_Key_Size": public_size
    }

if __name__ == "__main__":
    result = rsa_benchmark()
    print(result)