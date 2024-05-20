#!/bin/bash

mass_ranges=("0_500" "500_750" "750_1000" "1000_1500" "1500Inf")
lepton_flavors=("muon" "ele")
regions=("SR" "CR1" "CR2")
years=("UL18", "UL17", "UL16pre", "UL16post")

for year in "${years[@]}"; do
    for mass_range in "${mass_ranges[@]}"; do
        for lepton_flavor in "${lepton_flavors[@]}"; do
            for region in "${regions[@]}"; do
            #   python combine_input_file_withflags.py -m "$mass_range" -l "$lepton_flavor" -r "$region" -y "$year"
            python combine_input_file_withflags.py -m "$mass_range" -l "$lepton_flavor" -r "$region"
      done
    done
  done
done
