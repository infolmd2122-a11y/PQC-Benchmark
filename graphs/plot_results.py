import matplotlib.pyplot as plt
import pandas as pd

# =========================
# DATA (from your benchmark)
# =========================
data = [
    {"Algorithm": "RSA-2048", "KeyGen": 0.433086, "KeySize": 450, "Sign": None, "Verify": None},
    {"Algorithm": "ECC-P256", "KeyGen": 0.021669, "KeySize": 32, "Sign": None, "Verify": None},
    {"Algorithm": "Kyber512", "KeyGen": 0.000634, "KeySize": 800, "Sign": 0.000077, "Verify": 0.000014},
    {"Algorithm": "Dilithium2", "KeyGen": 0.015245, "KeySize": 1952, "Sign": 0.000446, "Verify": 0.000062},
]

df = pd.DataFrame(data)

# =========================
# 1. KEY GENERATION TIME
# =========================
plt.figure()
plt.bar(df["Algorithm"], df["KeyGen"])
plt.title("Key Generation Time Comparison")
plt.ylabel("Time (seconds)")
plt.xticks(rotation=30)
plt.tight_layout()
plt.savefig("graphs/keygen_time.png")
plt.show()

# =========================
# 2. KEY SIZE COMPARISON
# =========================
plt.figure()
plt.bar(df["Algorithm"], df["KeySize"])
plt.title("Key Size Comparison")
plt.ylabel("Bytes")
plt.xticks(rotation=30)
plt.tight_layout()
plt.savefig("graphs/key_size.png")
plt.show()

# =========================
# 3. SIGNATURE / CRYPTO OPS
# =========================
labels = ["Kyber Encap", "Kyber Decap", "Dilithium Sign", "Dilithium Verify"]
values = [
    df.loc[df["Algorithm"] == "Kyber512", "Sign"].values[0],
    df.loc[df["Algorithm"] == "Kyber512", "Verify"].values[0],
    df.loc[df["Algorithm"] == "Dilithium2", "Sign"].values[0],
    df.loc[df["Algorithm"] == "Dilithium2", "Verify"].values[0],
]

plt.figure()
plt.bar(labels, values)
plt.title("Post-Quantum Cryptographic Operations Time")
plt.ylabel("Time (seconds)")
plt.xticks(rotation=30)
plt.tight_layout()
plt.savefig("graphs/pqc_operations.png")
plt.show()