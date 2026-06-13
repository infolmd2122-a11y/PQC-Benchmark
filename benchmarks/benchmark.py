import subprocess

print("=== PQC BENCHMARK START ===")

print("Kyber running...")
subprocess.run(["python3", "benchmarks/kyber.py"])
print("Kyber done")

print("Dilithium running...")
subprocess.run(["python3", "benchmarks/dilithium.py"])
print("Dilithium done")

print("SPHINCS running...")
subprocess.run(["python3", "benchmarks/sphincs.py"])
print("SPHINCS done")

print("McEliece running...")
subprocess.run(["python3", "benchmarks/mceliece.py"])
print("McEliece done")

print("=== DONE ===")