# InterProScan Protein Annotation Pipeline

This repository provides a reproducible workflow to annotate proteins from **PlasmoDB** (or other organisms) using **InterProScan**.
It supports both:

* **Standalone installation** of InterProScan
* **Containerized execution** with **apptainer** (recommended for HPC or server environments)


## Features
  - Download protein FASTA sequences from PlasmoDB
  - Preprocess FASTA files (remove non-amino acid characters, uppercase sequences)
  - Run InterProScan analysis for each input FASTA file
  - Generate outputs in TSV format with protein domain annotations


## Requirements

* **RealVNC Viewer** (for accessing NMRBox, if using their resources)
* **NMRBox** account & credentials (**NMRHub**)
* **Apptainer** (instead of Singularity)
* **Linux environment** or **HPC cluster**


## Setup

### 1. Connect to NMRBox

1.  Install **RealVNC Viewer**.
2.  Log in with your **NMRHub** credentials.
3.  Start a new connection and select a software machine (named after an element).

### 2. Standalone Installation (no container)

Follow the **InterProScan standalone installation guide** (https://interproscan-docs.readthedocs.io/en/v5/UserDocs.html#obtaining-a-copy-of-interproscan).

Example run:

```bash
./interproscan.sh \
  -i data/fasta_files/PlasmoDB-67_Pfalciparum3D7_AnnotatedProteins.fasta \
  -o output/resultados_1.tsv \
  -f tsv
```

### 3. Containerized Execution (recommended)
Follow the **InterProScan installation via Container** (https://interproscan-docs.readthedocs.io/en/v5/HowToUseViaContainer.html)

**Pull the InterProScan image**

```bash
apptainer pull docker://interproscan/interproscan
```

**Preprocess FASTA**

```bash
cd input

awk '/^>/ {if(NR>1) printf("\n"); print $1; next} {printf("%s", toupper($0))} END {printf("\n")}' PlasmoDB-67_PyoeliiyoeliiYM_AnnotatedProteins.fasta | \
sed '/^>/! s/[^A-Z]//g' > PlasmoDB-67_PyoeliiyoeliiYM.fasta

cd ..
```

**Run InterProScan**

```bash
apptainer exec \
  -B $PWD/interproscan-5.74-105.0/data:/opt/interproscan/data \
  -B $PWD/input:/input \
  -B $PWD/temp:/temp \
  -B $PWD/output:/output \
  interproscan_latest.sif \
  /opt/interproscan/interproscan.sh \
  --input /input/PlasmoDB-67_PyoeliiyoeliiYM.fasta \
  --output-dir /output/PlasmoDB-67_PyoeliiyoeliiYM \
  --tempdir /temp \
  --cpu 8
  ```

### See executable script:
workflows/run_interproscan.sh


## References

* **InterProScan Documentation** (https://interproscan-docs.readthedocs.io/en/v5/)
* **PlasmoDB** (https://plasmodb.org/plasmo/app)
* **NMRBox** (https://nmrbox.nmrhub.org/)