import oqs
import time


def dilithium_benchmark():

    sig = oqs.Signature("ML-DSA-65")

    # Key generation
    start = time.time()
    public_key = sig.generate_keypair()
    keygen_time = time.time() - start

    message = b"Post-Quantum Crypto Benchmark"

    # Signing
    start = time.time()
    signature = sig.sign(message)
    sign_time = time.time() - start

    # Verification
    start = time.time()
    valid = sig.verify(message, signature, public_key)
    verify_time = time.time() - start

    sig.free()

    return {
        "Algorithm": "Dilithium2",
        "KeyGen_Time": keygen_time,
        "Sign_Time": sign_time,
        "Verify_Time": verify_time,
        "Key_Size": len(public_key),
        "Signature_Size": len(signature),
        "Valid": valid
    }


if __name__ == "__main__":
    result = dilithium_benchmark()
    print(result)