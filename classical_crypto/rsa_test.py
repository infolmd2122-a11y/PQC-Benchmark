from Crypto.PublicKey import RSA
import time

def rsa_benchmark():

    start = time.time()
    key = RSA.generate(2048)
    keygen_time = time.time() - start

    private_key = key.export_key()
    public_key = key.publickey().export_key()

    return {
        "Algorithm": "RSA-2048",
        "KeyGen_Time": keygen_time,
        "Key_Size": len(public_key)
    }

if __name__ == "__main__":
    result = rsa_benchmark()
    print(result)