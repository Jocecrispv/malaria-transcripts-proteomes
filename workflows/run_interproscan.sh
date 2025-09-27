#!/bin/bash
# run_interproscan.sh

# Script to run InterProScan on a given FASTA file
# using Apptainer (Singularity-compatible container).
# 
# This script mounts the necessary directories and
# executes InterProScan with multi-threading support.

# Exit immediately if a command exits with a non-zero status
set -e


# Configuration variables

# Change these paths if your directories differ

# Local path to InterProScan container image
INTERPROSCAN_CONTAINER="interproscan_latest.sif"

# Directory containing InterProScan data files
INTERPROSCAN_DATA="$PWD/interproscan-5.74-105.0/data"

# Directory with input FASTA files
INPUT_DIR="$PWD/input"

# Temporary directory for InterProScan
TEMP_DIR="$PWD/temp"

# Output directory for results
OUTPUT_DIR="$PWD/output"

# Input FASTA file to analyze (change filename as needed)
FASTA_FILE="PlasmoDB-67_PyoeliiyoeliiYM.fasta"

# Number of CPU threads to use
CPU=8


# Run InterProScan

echo "Running InterProScan for file: $FASTA_FILE"
echo "Output will be saved in: $OUTPUT_DIR"

apptainer exec \
  -B "$INTERPROSCAN_DATA":/opt/interproscan/data \  # Mount InterProScan data
  -B "$INPUT_DIR":/input \                           # Mount input directory
  -B "$TEMP_DIR":/temp \                             # Mount temporary directory
  -B "$OUTPUT_DIR":/output \                         # Mount output directory
  "$INTERPROSCAN_CONTAINER" \                        # Specify container image
  /opt/interproscan/interproscan.sh \               # InterProScan executable
  --input "/input/$FASTA_FILE" \                    # Input FASTA file inside container
  --output-dir "/output/${FASTA_FILE%.*}" \         # Output directory (named after FASTA)
  --tempdir /temp \                                 # Temporary directory inside container
  --cpu "$CPU"                                      # Number of CPU threads

echo "InterProScan analysis completed successfully!"
echo "Results can be found in: $OUTPUT_DIR/${FASTA_FILE%.*}"
