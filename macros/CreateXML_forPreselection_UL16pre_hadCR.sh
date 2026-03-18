#!/bin/bash 

echo "initial dir: $PWD"

# Enable recursive globbing (globstar)
shopt -s globstar

# Where UHH2 code is installed
pathGL_code="/data/dust/user/titasroy/Ac_UL/CMSSW_10_6_28/src/UHH2/"
# Where (NOT MERGED) trees - preselection stored

path_data="/pnfs/desy.de/cms/tier2/store/group/uhh/uhh2ntuples/RunII_106X_v2/UL17/TTToHadronic_TuneCP5CR2_13TeV-powheg-pythia8/crab_TTToHadronic_CP5CR2_powheg-pythia8_Summer20UL17_v2/220116_203424/"

# Define the output directory
output_dir="$pathGL_code/ZprimeSemiLeptonic/data/Skimming_datasets_UL17_CR_preselection/"

# Create the output directory if it doesn't exist
mkdir -p "$output_dir"
cd "$output_dir" || { echo "Failed to enter directory: $output_dir"; exit 1; }

samples=("TTToHadronic_TuneCP5CR2")



# Loop over each sample
for sample_name in "${samples[@]}"
do
    echo "Processing sample: $sample_name"

    root_pattern="${path_data}/**/Ntuple_*.root"
    #echo $root_pattern
    matched_files=( $root_pattern )
    if [ ${#matched_files[@]} -eq 0 ]; then
        echo "No Ntuple_*.root files found in $path_data"
        continue
    fi

    echo "Found ${#matched_files[@]} ROOT files for sample $sample_name."

    echo "dir now: $PWD"
    cd "$output_dir"
    # echo " running from dir: $PWD"
    "$pathGL_code/scripts/create-dataset-xmlfile" "$root_pattern" "MC_${sample_name}.xml"

    if [ ! -f "MC_${sample_name}.xml" ]; then
        echo "Failed to create XML file for sample $sample_name."
        continue
    fi
    cd "$pathGL_code/ZprimeSemiLeptonic/macros" || { echo "Failed to enter macros directory."; exit 1; }

    echo "XML file MC_${sample_name}.xml created successfully."

    # Update the XML file with event counts
    python "$pathGL_code/scripts/crab/readaMCatNloEntries.py" 10 "$output_dir/MC_${sample_name}.xml" False

    if [ $? -ne 0 ]; then
        echo "readaMCatNloEntries.py failed for sample $sample_name."
        continue
    fi

    echo "Processed sample $sample_name successfully."

done

# # Return to the macros directory
pwd
cd "$pathGL_code/ZprimeSemiLeptonic/macros" || { echo "Failed to enter macros directory."; exit 1; }
