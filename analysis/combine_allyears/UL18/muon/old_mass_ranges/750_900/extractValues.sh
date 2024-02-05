#!/bin/bash

flavor="muon"
mass="750-900"

FILEPATH="higgsCombine_initialFit_Test.MultiDimFit.mH125.root"

root -l -b -q <<EOF
.L extractValues.C+
extractValues("$FILEPATH");
EOF
