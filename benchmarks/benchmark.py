import pandas as pd

from classical_crypto.rsa_test import rsa_benchmark
from classical_crypto.ecc_test import ecc_benchmark
from post_quantum.kyber_test import kyber_benchmark


def run_all():

    results = []

    results.append(rsa_benchmark())
    results.append(ecc_benchmark())
    results.append(kyber_benchmark())

    return results


if __name__ == "__main__":

    results = run_all()

    df = pd.DataFrame(results)

    print("\n=== RESULTS ===\n")
    print(df)

    df.to_csv("results/benchmark_results.csv", index=False)