import FWCore.ParameterSet.Config as cms
from UHH2.core.ntuple_generator import generate_process  # use CMSSW type path for CRAB
from UHH2.core.optionsParse import setup_opts, parse_apply_opts
import sys


"""NTuple config for UL18 MC datasets.

You should try and put any centralised changes in generate_process(), not here.
"""


process = generate_process(year="UL18", useData=False)

process = generate_process(year="UL18", useData=False)

if len(sys.argv) > 3:
    input_file = sys.argv[2]
    output_file = sys.argv[3]
    process.source.fileNames = cms.untracked.vstring(input_file)
    process.TFileService = cms.Service("TFileService",
                                       fileName = cms.string(output_file))
else:
    print("Error: The script expects at least two arguments - input file and output file.")
    sys.exit(1)

print("Input file set to:", input_file)
print("Output file set to:", output_file)

# if len(sys.argv) > 1:
#     input_file = sys.argv[1]
#     process.source.fileNames = cms.untracked.vstring(input_file)



print(sys.argv)
# Do this after setting process.source.fileNames, since we want the ability to override it on the commandline
options = setup_opts(output_file)
parse_apply_opts(process, options)

with open('pydump_mc_UL18.py', 'w') as f:
    f.write(process.dumpPython())

