import oqs
import time


def kyber_benchmark():

    kem = oqs.KeyEncapsulation("Kyber512")

    # Key generation time
    start = time.time()
    public_key = kem.generate_keypair()
    keygen_time = time.time() - start

    # Encapsulation time
    start = time.time()
    ciphertext, shared_secret_enc = kem.encap_secret(public_key)
    encap_time = time.time() - start

    # Decapsulation time
    start = time.time()
    shared_secret_dec = kem.decap_secret(ciphertext)
    decap_time = time.time() - start

    kem.free()

    return {
        "Algorithm": "Kyber512",
        "KeyGen_Time": keygen_time,
        "Encap_Time": encap_time,
        "Decap_Time": decap_time,
        "Key_Size": len(public_key)
    }


if __name__ == "__main__":
    result = kyber_benchmark()
    print(result)