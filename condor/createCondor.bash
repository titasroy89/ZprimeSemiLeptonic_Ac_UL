#!/bin/bash

cat > condor_job.sub <<EOL
Universe = vanilla
Executable = run_on_condor.sh
output = \$(Cluster)_\$(Process).out
error = \$(Cluster)_\$(Process).err
log = \$(Cluster)_\$(Process).log
Transfer_Input_Files = EFT_nanofiles_fully_semileptonic_multiprocess.py
WhenToTransferOutput = ON_EXIT
EOL

for file in /nfs/dust/cms/user/beozek/uuh2-106X_v2/CMSSW_10_6_28/src/UHH2/core/python/ntuplewriter_mc_UL18.py; do
    echo "arguments = $(basename $file)" >> condor_job.sub
    echo "Queue" >> condor_job.sub
done