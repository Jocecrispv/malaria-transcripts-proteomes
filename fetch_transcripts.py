#!/usr/bin/env python3

"""
fetch_transcripts.py
--------------------
Download high-quality canonical transcripts for malaria species from PlasmoDB.
"""

import requests
import json
from urllib.parse import quote
import argparse
import sys


def fetch_transcripts(organism, output_file):
    """Fetch high-quality canonical transcripts from PlasmoDB for a given organism."""

    # API configuration
    base_url = "https://plasmodb.org/plasmo/service"
    endpoint = "/record-types/transcript/searches/GenesByTaxon/reports/gff3"

    # Organism must be a JSON array
    organism_json = json.dumps([organism])

    # Report filters
    report_config = {
        "includeSeq": False,
        "type": "transcript",
        "track": "gene",
        "filters": {
            "annotation_quality": ["high"],
            "evidence": ["RNA-Seq"],
            "transcript_status": ["canonical"],
        },
    }

    params = {
        "organism": organism_json,
        "reportConfig": json.dumps(report_config),
    }

    # Build request URL
    api_url = (
        f"{base_url}{endpoint}"
        f"?organism={quote(params['organism'])}"
        f"&reportConfig={quote(params['reportConfig'])}"
    )

    try:
        response = requests.get(api_url, timeout=80)

        if response.status_code == 200:
            with open(output_file, "wb") as f:
                f.write(response.content)
            print(f"Success! Filtered GFF3 saved to {output_file}")
        else:
            print(f"Error {response.status_code}: {response.text}")
            sys.exit(1)

    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
        sys.exit(1)


def main():
    parser = argparse.ArgumentParser(
        description="Download high-quality canonical transcripts from PlasmoDB."
    )
    parser.add_argument(
        "-o", "--organism",
        type=str,
        required=True,
        help="Organism name (e.g., 'Plasmodium falciparum 3D7')."
    )
    parser.add_argument(
        "-f", "--file",
        type=str,
        default="transcripts.gff3",
        help="Output filename (default: transcripts.gff3)."
    )

    args = parser.parse_args()
    fetch_transcripts(args.organism, args.file)


if __name__ == "__main__":
    main()
