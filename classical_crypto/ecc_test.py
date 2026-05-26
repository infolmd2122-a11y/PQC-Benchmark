from cryptography.hazmat.primitives.asymmetric import ec
import time

def ecc_benchmark():

    start = time.time()
    key = ec.generate_private_key(ec.SECP256R1())
    keygen_time = time.time() - start

    return {
        "Algorithm": "ECC-P256",
        "KeyGen_Time": keygen_time,
        "Key_Size": 32  # ثابت (compressed point size)
    }

if __name__ == "__main__":
    result = ecc_benchmark()
    print(result)