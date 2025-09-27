# Malaria Transcripts & Proteomes Analysis

This repository provides **Python scripts** and **workflow instructions** to download and annotate **malaria proteomes and transcripts** for malaria species (or other organisms available in [PlasmoDB / VEuPathDB](https://plasmodb.org/)).

It covers:

1. **Downloading canonical transcripts** in **GFF3 format**  
2. **Downloading proteomes** in **FASTA format**  
3. **Functional annotation** using **InterProScan** (standalone or containerized)


## Included Scripts

### 1. Transcript Downloader (`scripts/transcript_downloader.py`)
- Downloads **canonical transcripts** filtered by:
  - High annotation quality  
  - RNA-Seq evidence  
  - Canonical transcript status  
- Output format: **GFF3**  
- Suitable for **genomics pipelines** and **malaria transcriptomics research**.
- Command-line usage:

```bash
python scripts/transcript_downloader.py "Plasmodium falciparum 3D7"```


### 2. Proteome Downloader (`scripts/proteome_downloader.py`)

- Downloads **protein sequences (proteomes)** in **FASTA format**.  
- Works for **any Plasmodium species** or other organisms in PlasmoDB.  
- Automatically names files based on species, e.g.:  
  - `Plasmodium_falciparum_3D7_proteome.fasta`  
  - `Plasmodium_ovale_curtisi_GH01_proteome.fasta`

**Command-line usage:**

```bash
python scripts/proteome_downloader.py "Plasmodium vivax P01"```

###  Protein Functional Annotation with InterProScan

Step-by-step instructions for annotating downloaded proteomes are included in the workflow guide:  
    [InterProScan Workflow Guide](workflows/interproscan_instructions.md)
    
    This guide covers both:
    - **Standalone installation**  
    - **Containerized execution using Apptainer/Singularity**

## Features

- Query PlasmoDB API directly from Python.  
- Customizable organism input (e.g., *Plasmodium falciparum*, *Plasmodium vivax*) via command-line.  
- Saves transcripts as `.gff3` and proteomes as `.fasta`.
- Annotate proteins with InterProScan for functional analysis.  
- Works on Linux, macOS, and Windows.  

## Requirements

- Python 3.7+  
- `requests` library  

Install dependencies:  

```bash
pip install requests```

- For InterProScan:
    - Standalone: Java & local installation
    - Containerized: Apptainer/Singularity


### Example Workflow

1. **Download transcripts:**

```bash
python scripts/transcript_downloader.py -o "Plasmodium falciparum 3D7" -f Pf3D7_transcripts.gff3 ```

2. Download proteome:

```bash
python scripts/proteome_downloader.py "Plasmodium falciparum 3D7"```

3. Run InterProScan annotation:

# See full instructions:
workflows/interproscan_instructions.md
