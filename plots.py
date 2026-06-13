import pandas as pd
import matplotlib.pyplot as plt
import os

# =========================
# CREATE OUTPUT FOLDER
# =========================
os.makedirs("graphs", exist_ok=True)

# =========================
# FILES
# =========================
summary_files = {
    "Kyber": "kyber_summary.csv",
    "Dilithium": "dilithium_summary.csv",
    "SPHINCS+": "sphincs_summary.csv",
    "McEliece": "mceliece_summary.csv"
}

memory_files = {
    "Kyber": "kyber_memory.csv",
    "Dilithium": "dilithium_memory.csv",
    "SPHINCS+": "sphincs_memory.csv",
    "McEliece": "mceliece_memory.csv"
}


# =========================
# FUNCTION TO EXTRACT MEAN
# =========================
def get_mean(file, operation):
    try:
        df = pd.read_csv(file)
        row = df[df["Operation"] == operation]

        if row.empty:
            return None

        return float(row.iloc[0]["Mean"])

    except:
        return None


# =========================
# KEY GENERATION GRAPH
# =========================
algorithms = []
values = []

for alg, file in summary_files.items():
    val = get_mean(file, "KeyGen")

    if val is not None:
        algorithms.append(alg)
        values.append(val)

plt.figure()
plt.bar(algorithms, values)

plt.title("Key Generation Time Comparison")
plt.ylabel("Time (ms)")

plt.savefig("graphs/keygen_comparison.png")
plt.close()


# =========================
# ENCAPSULATION GRAPH
# =========================
algorithms = []
values = []

for alg, file in summary_files.items():

    val = get_mean(file, "Encapsulation")

    if val is None:
        val = get_mean(file, "Encryption")

    if val is not None:
        algorithms.append(alg)
        values.append(val)

plt.figure()
plt.bar(algorithms, values)

plt.title("Encapsulation / Encryption Time Comparison")
plt.ylabel("Time (ms)")

plt.savefig("graphs/encapsulation_comparison.png")
plt.close()


# =========================
# DECAPSULATION GRAPH
# =========================
algorithms = []
values = []

for alg, file in summary_files.items():

    val = get_mean(file, "Decapsulation")

    if val is None:
        val = get_mean(file, "Decryption")

    if val is not None:
        algorithms.append(alg)
        values.append(val)

plt.figure()
plt.bar(algorithms, values)

plt.title("Decapsulation / Decryption Time Comparison")
plt.ylabel("Time (ms)")

plt.savefig("graphs/decapsulation_comparison.png")
plt.close()


# =========================
# SIGNATURE GENERATION GRAPH
# =========================
algorithms = []
values = []

for alg, file in summary_files.items():

    val = get_mean(file, "Sign")

    if val is not None:
        algorithms.append(alg)
        values.append(val)

plt.figure()
plt.bar(algorithms, values)

plt.title("Signature Generation Time Comparison")
plt.ylabel("Time (ms)")

plt.savefig("graphs/signature_generation.png")
plt.close()


# =========================
# VERIFICATION GRAPH
# =========================
algorithms = []
values = []

for alg, file in summary_files.items():

    val = get_mean(file, "Verify")

    if val is not None:
        algorithms.append(alg)
        values.append(val)

plt.figure()
plt.bar(algorithms, values)

plt.title("Signature Verification Time Comparison")
plt.ylabel("Time (ms)")

plt.savefig("graphs/verification.png")
plt.close()


# =========================
# MEMORY GRAPHS
# =========================

parameters = [
    "Public Key",
    "Private Key",
    "Ciphertext",
    "Signature"
]

for parameter in parameters:

    algorithms = []
    values = []

    for alg, file in memory_files.items():

        try:
            df = pd.read_csv(file)

            row = df[df["Parameter"] == parameter]

            if not row.empty:
                algorithms.append(alg)
                values.append(float(row.iloc[0]["Size(Bytes)"]))

        except:
            pass

    if values:

        plt.figure()
        plt.bar(algorithms, values)

        plt.title(f"{parameter} Size Comparison")
        plt.ylabel("Bytes")

        filename = parameter.lower().replace(" ", "_")

        plt.savefig(f"graphs/{filename}.png")
        plt.close()


# =========================
# TOTAL MEMORY GRAPH
# =========================
algorithms = []
totals = []

for alg, file in memory_files.items():

    try:
        df = pd.read_csv(file)

        total = df["Size(Bytes)"].sum()

        algorithms.append(alg)
        totals.append(total)

    except:
        pass


plt.figure()
plt.bar(algorithms, totals)

plt.title("Total Memory Consumption Comparison")
plt.ylabel("Bytes")

plt.savefig("graphs/memory_consumption.png")
plt.close()


print("All graphs generated successfully.")