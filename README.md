# PQC Benchmark Project

## Project Structure

```
PQC-Benchmark/
│
├── benchmarks/
│   ├── kyber.py
│   ├── dilithium.py
│   ├── sphincs.py
│   ├── mceliece.py
│   ├── benchmark.py
│
├── graphs/
│   ├── (generated PNG files)
│
├── results/
│   ├── kyber_summary.csv
│   ├── dilithium_summary.csv
│   ├── sphincs_summary.csv
│   ├── mceliece_summary.csv
│
├── requirements.txt
├── README.md
├── run.sh
└── plots.py
```

## Description

This project implements an experimental evaluation of post-quantum cryptographic algorithms using the Open Quantum Safe (liboqs) library and its Python bindings.

The evaluated algorithms are:

* Kyber (KEM)
* Dilithium (Digital Signature)
* SPHINCS+ (Digital Signature)
* Classic McEliece (KEM)

Each experiment is executed 100 times. The following statistical measures are computed:

* Mean
* Minimum
* Maximum
* Standard deviation

Performance graphs are automatically generated from the collected results.

## Experimental Environment

The project was developed and tested under:

* Windows 11
* WSL2 with Ubuntu 24.04
* Python 3.12

## Installation

### 1. Clone the repository

```bash
git clone <repository-url>
cd PQC-Benchmark
```

### 2. Create a virtual environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install the required dependencies

```bash
pip install -r requirements.txt
```

## Running the benchmarks

Execute all benchmark scripts:

```bash
python3 -m benchmarks.benchmark
```

## Generating graphs

```bash
python3 plots.py
```

The generated graphs will be stored in the `graphs/` directory.

## Output Files

The project generates:

* Raw CSV files containing the measurements of each run;
* Summary CSV files containing mean, minimum, maximum and standard deviation;
* Graphs comparing the different algorithms.

## Reproducibility

The project relies on official implementations provided by Open Quantum Safe (liboqs). All scripts, dependencies and execution instructions are provided to ensure that the experimental results can be reproduced on a different machine.
