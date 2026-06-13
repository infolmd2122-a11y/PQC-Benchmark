import oqs
import time
import statistics
import csv

ALGORITHM = "SPHINCS+-SHA2-128f-simple"
RUNS = 100

sig = oqs.Signature(ALGORITHM)

keygen_times = []
sign_times = []
verify_times = []

raw_file = open("sphincs_raw.csv", "w", newline="")
writer = csv.writer(raw_file)
writer.writerow(["Operation", "Run", "Time(ms)"])

message = b"benchmark test"

# KEYGEN
for i in range(RUNS):
    start = time.perf_counter()
    public_key = sig.generate_keypair()
    end = time.perf_counter()

    keygen_times.append((end - start) * 1000)
    writer.writerow(["KeyGen", i+1, (end - start) * 1000])

# SIGN
for i in range(RUNS):
    public_key = sig.generate_keypair()
    signature = sig.sign(message)

    start = time.perf_counter()
    sig.sign(message)
    end = time.perf_counter()

    sign_times.append((end - start) * 1000)
    writer.writerow(["Sign", i+1, (end - start) * 1000])

# VERIFY
for i in range(RUNS):
    public_key = sig.generate_keypair()
    signature = sig.sign(message)

    start = time.perf_counter()
    sig.verify(message, signature, public_key)
    end = time.perf_counter()

    verify_times.append((end - start) * 1000)
    writer.writerow(["Verify", i+1, (end - start) * 1000])

raw_file.close()

def stats(data):
    return [statistics.mean(data), min(data), max(data), statistics.stdev(data)]

with open("sphincs_summary.csv", "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["Operation", "Mean", "Min", "Max", "Std"])
    w.writerow(["KeyGen"] + stats(keygen_times))
    w.writerow(["Sign"] + stats(sign_times))
    w.writerow(["Verify"] + stats(verify_times))

print("SPHINCS done")

with open("sphincs_memory.csv", "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["Parameter", "Size(Bytes)"])

    details = sig.details

    w.writerow(["Public Key", details["length_public_key"]])
    w.writerow(["Private Key", details["length_secret_key"]])
    w.writerow(["Signature", details["length_signature"]])