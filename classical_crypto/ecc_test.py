import time
from cryptography.hazmat.primitives.asymmetric import ec

def ecc_benchmark():
    start = time.time()

    private_key = ec.generate_private_key(
        ec.SECP256R1()
    )

    end = time.time()

    execution_time = end - start

    return {
        "Algorithm": "ECC-P256",
        "KeyGen_Time": execution_time
    }

if __name__ == "__main__":
    result = ecc_benchmark()
    print(result)