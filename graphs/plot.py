import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("results/results.csv")

plt.figure(figsize=(8,5))

plt.bar(df["Algorithm"], df["KeyGen_Time"])

plt.xlabel("Algorithm")
plt.ylabel("Execution Time")
plt.title("Key Generation Benchmark")

plt.savefig("graphs/keygen_benchmark.png")

plt.show()