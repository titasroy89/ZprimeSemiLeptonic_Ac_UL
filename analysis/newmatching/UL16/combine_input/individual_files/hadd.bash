#!/bin/bash

categories=(
  "ele_0_500"
  "ele_500_750"
  "ele_750_1000"
  "ele_1000_1500"
  "ele_1500Inf"
  "muon_0_500"
  "muon_500_750"
  "muon_750_1000"
  "muon_1000_1500"
  "muon_1500Inf"
)

regions=(
  "CR1"
  "CR2"
  "SR"
)

input_dir="./prepost"

for category in "${categories[@]}"; do
  for region in "${regions[@]}"; do
    output_file="dY_UL16_${category}_${region}.root"
    
    preVFP_file="${input_dir}/dY_UL16preVFP_${category}_${region}.root"
    postVFP_file="${input_dir}/dY_UL16postVFP_${category}_${region}.root"
    
    if [[ -f "$preVFP_file" && -f "$postVFP_file" ]]; then
      hadd "$output_file" "$preVFP_file" "$postVFP_file"
      echo "Created $output_file"
    else
      echo "Skipping $output_file: One or both input files are missing"
      if [[ ! -f "$preVFP_file" ]]; then
        echo "  Missing file: $preVFP_file"
      fi
      if [[ ! -f "$postVFP_file" ]]; then
        echo "  Missing file: $postVFP_file"
      fi
    fi
  done
done
