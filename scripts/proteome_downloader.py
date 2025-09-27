#!/usr/bin/env python3

import requests
import json
import sys
from urllib.parse import quote

def download_plasmodb_proteome(organism_name):
    """
    Download the proteome of a given Plasmodium species from PlasmoDB.
    
    Parameters:
        organism_name (str): Scientific name of the Plasmodium organism, 
                             e.g. "Plasmodium falciparum 3D7"
    """
    # Base API configuration
    base_url = "https://plasmodb.org/plasmo/service"
    endpoint = "/record-types/transcript/searches/GenesByTaxon/reports/sequence"
    
    # API config
    config = {
        "searchConfig": {
            "parameters": {
                "organism": [organism_name]
            },
            "wdkWeight": 10
        },
        "reportConfig": {
            "attachmentType": "text",
            "deflineType": "full",
            "deflineFields": [
                "gene_id",
                "organism",
                "description",
                "position",
                "ui_choice",
                "segment_length"
            ],
            "sequenceFormat": "fasta",
            "basesPerLine": 60,
            "type": "protein",
            "reverseAndComplement": False,
            "upstreamAnchor": "Start",
            "upstreamSign": "plus",
            "upstreamOffset": 0,
            "downstreamAnchor": "End",
            "downstreamSign": "plus",
            "downstreamOffset": 0,
            "startAnchor3": "DownstreamFromStart",
            "startOffset3": 0,
            "endAnchor3": "UpstreamFromEnd",
            "endOffset3": 0,
            "dnaComponent": "exon",
            "transcriptComponent": "five_prime_utr",
            "proteinFeature": "interpro",
            "splicedGenomic": "cds"
        }
    }

    # Prepare parameters
    params = {
        "organism": json.dumps(config["searchConfig"]["parameters"]["organism"]),
        "reportConfig": json.dumps(config["reportConfig"], separators=(',', ':'))
    }

    # Construct URL
    try:
        api_url = (
            f"{base_url}{endpoint}"
            f"?organism={quote(params['organism'])}"
            f"&reportConfig={quote(params['reportConfig'])}"
        )
    except Exception as e:
        print(f"URL construction failed: {e}")
        return False

    # Make request with error handling
    try:
        response = requests.get(api_url, timeout=30)
        
        if response.status_code == 200 and response.text.strip():
            # Clean filename (replace spaces with underscores)
            filename = organism_name.replace(" ", "_") + "_proteome.fasta"
            
            # Save the protein sequences
            with open(filename, "w") as f:
                f.write(response.text)
            
            # Count sequences and report success
            num_sequences = response.text.count('>')
            print(f"Success! Downloaded {num_sequences} protein sequences for {organism_name}.")
            print(f"Saved as: {filename}")
            return True
            
        else:
            print(f"Error {response.status_code}: {response.text}")
            return False
            
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
        return False


# Run from command line
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python proteome_downloader.py 'Plasmodium falciparum 3D7'")
    else:
        organism = " ".join(sys.argv[1:])
        download_plasmodb_proteome(organism)
