#!/bin/bash

# Define the data directory and expected output files
DATA_DIR="data"
EXPECTED_FILES=("INDTemperature.csv" "INDFloods.csv" "INDImportExport.csv")

# Run the data pipeline
echo "Running data pipeline..."
python3 pipeline.py

# Check for the existence of the output files
for file in "${EXPECTED_FILES[@]}"; do
    if [ -f "$DATA_DIR/$file" ]; then
        echo "Test passed: $file exists."
    else
        echo "Test failed: $file does not exist."
        exit 1
    fi
done

echo "All tests passed."
exit 0
