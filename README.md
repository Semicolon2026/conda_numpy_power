# conda_numpy_power

A Conda-based containerized environment designed for **security validation, CVE analysis, SBOM comparison, and cross-architecture testing** using `numpy` as the core dependency.

This project is intentionally structured to simulate a **vulnerable dependency baseline image** for security and supply-chain testing workflows.

---

## 🎯 Purpose

This repository is used for:

- CVE scanning validation in Conda environments
- SBOM generation and comparison
- POWER vs x86 architecture vulnerability analysis
- Dependency remediation testing workflows
- Security regression testing for scientific Python stacks

---

## 🧱 Core Stack

- Conda (Miniconda base image)
- Python 3.10/3.11 (via Conda)
- NumPy (primary dependency)
- Pandas
- PyYAML
- scikit-learn (optional ML dependency layer)

---

## 🐳 Container Use Case

This image is designed to simulate a **real-world Conda ML environment** that is commonly used in:

- Data science workloads
- ML pipelines
- Scientific computing environments

which often introduce **high CVE surface area via native dependencies**.

---

## 🚀 Build Image

```bash
docker build -t conda-numpy-power .
