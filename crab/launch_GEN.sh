#!/bin/sh

dir="/nfs/dust/cms/user/beozek/uuh2-106X_v2/CMSSW_10_6_28/src/UHH2/ZprimeSemiLeptonic/crab/"

python launch_GEN.py $@ --production_label TT01j1lCA_NoHT --unitsPerJob 2500 --totalUnits 1000000 --publish --gridpackDir ${dir} --gridpack TT01j1lCA_slc7_amd64_gcc700_CMSSW_10_6_19_tarball.tar.xz


# python launch_GEN.py $@ --config gen_LO_01j_mc_102X_CP5 --production_label PNet_TT01j1l_HT800-ext --unitsPerJob 30000 --totalUnits 20000000 --publish --gridpackDir ${dir} --gridpack TT01j1l_HT800_slc7_amd64_gcc700_CMSSW_10_6_19_tarball.tar.xz 
