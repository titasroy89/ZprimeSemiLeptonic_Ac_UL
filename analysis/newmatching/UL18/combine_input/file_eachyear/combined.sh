#!/bin/bash

mass_ranges=("0_500" "500_750" "750_1000" "1000_1500" "1500Inf")
lepton_flavors=("muon" "ele")
regions=("SR" "CR1" "CR2")
years=("UL18" "UL17" "UL16pre" "UL16post")


for mass_range in "${mass_ranges[@]}"; do
    echo "Processing mass range: $mass_range"
    python file_combined.py -m "$mass_range" -l "ele"
done
