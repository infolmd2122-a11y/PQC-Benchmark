import oqs
import time

def kyber_benchmark():
    start = time.time()

    kem = oqs.KeyEncapsulation("Kyber512")
    public_key = kem.generate_keypair()

    end = time.time()

    execution_time = end - start

    return {
        "Algorithm": "Kyber512",
        "KeyGen_Time": execution_time,
        "Public_Key_Size": len(public_key)
    }

if __name__ == "__main__":
    result = kyber_benchmark()
    print(result)