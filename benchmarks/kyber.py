import oqs
import time
import statistics
import csv

ALGORITHM = "Kyber512"
RUNS = 100

kem = oqs.KeyEncapsulation(ALGORITHM)

keygen_times = []
enc_times = []
dec_times = []

with open("kyber_raw.csv", "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["Operation", "Run", "Time(ms)"])

    for i in range(RUNS):
        start = time.perf_counter()
        pk = kem.generate_keypair()
        end = time.perf_counter()

        t = (end - start) * 1000
        keygen_times.append(t)
        w.writerow(["KeyGen", i+1, t])

    for i in range(RUNS):
        pk = kem.generate_keypair()

        start = time.perf_counter()
        ct, ss = kem.encap_secret(pk)
        end = time.perf_counter()

        t = (end - start) * 1000
        enc_times.append(t)
        w.writerow(["Encapsulation", i+1, t])

    for i in range(RUNS):
        pk = kem.generate_keypair()
        ct, ss = kem.encap_secret(pk)

        start = time.perf_counter()
        kem.decap_secret(ct)
        end = time.perf_counter()

        t = (end - start) * 1000
        dec_times.append(t)
        w.writerow(["Decapsulation", i+1, t])


def stats(x):
    return [statistics.mean(x), min(x), max(x), statistics.stdev(x) if len(x)>1 else 0]

with open("kyber_summary.csv", "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["Operation", "Mean", "Min", "Max", "Std"])
    w.writerow(["KeyGen"] + stats(keygen_times))
    w.writerow(["Encapsulation"] + stats(enc_times))
    w.writerow(["Decapsulation"] + stats(dec_times))

with open("kyber_memory.csv", "w", newline="") as f:
    w = csv.writer(f)
    d = kem.details
    w.writerow(["Parameter", "Size(Bytes)"])
    w.writerow(["Public Key", d["length_public_key"]])
    w.writerow(["Private Key", d["length_secret_key"]])
    w.writerow(["Ciphertext", d["length_ciphertext"]])

print("Kyber done")