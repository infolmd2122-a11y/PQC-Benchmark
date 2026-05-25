import pandas as pd

from classical_crypto.rsa_test import rsa_benchmark
from classical_crypto.ecc_test import ecc_benchmark
from post_quantum.kyber_test import kyber_benchmark

results = [
    rsa_benchmark(),
    ecc_benchmark(),
    kyber_benchmark()
]

df = pd.DataFrame(results)

print(df)

df.to_csv("results/results.csv", index=False)
