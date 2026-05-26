# PQC-Benchmark 🔐

Benchmarking Classical vs Post-Quantum Cryptography using Python and liboqs.

## 📌 Project Overview

This project compares classical cryptographic algorithms (RSA, ECC) with post-quantum algorithms (Kyber, Dilithium).

It evaluates:
- Key generation time
- Encryption / signature time
- Key sizes
- Signature sizes

## ⚙️ Technologies Used

- Python 3
- liboqs-python
- pycryptodome
- cryptography
- matplotlib
- pandas

## 📁 Project Structure



## 🚀 How to Run

```bash
pip install -r requirements.txt

python benchmarks/benchmark.py
python graphs/plot_results.py