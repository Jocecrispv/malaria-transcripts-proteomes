# malaria-transcripts
# Malaria Transcript Downloader

This project provides a **Python script** to download **high-quality canonical transcripts** for malaria species (or other organisms available in PlasmoDB/VEuPathDB).

It uses the [PlasmoDB API](https://plasmodb.org/) and applies filters to retrieve only transcripts with:

- High annotation quality  
- RNA-Seq evidence  
- Canonical transcript status  

The output is saved in **GFF3 format**, suitable for bioinformatics pipelines and malaria research.


## Features

- Query PlasmoDB API directly from Python.  
- Customizable organism input (e.g., *Plasmodium falciparum*, *Plasmodium vivax*).  
- Saves filtered results in `.gff3` format.  
- Easy command-line usage with `argparse`.  
- Works on Linux, macOS, and Windows.  


## Requirements

- Python 3.7+  
- `requests` library  

Install dependencies:  

```bash
pip install requests
