#!/bin/bash

echo "Checking Condor environment..."

# Source CMSSW environment
echo "Setting up CMSSW environment..."
source /cvmfs/cms.cern.ch/cmsset_default.sh
cd /data/dust/user/beozek/uuh2-106X_v2/CMSSW_10_6_28/src
eval `scramv1 runtime -sh`

# Check if condor_submit is available
echo "Checking for condor_submit..."
which condor_submit
if [ $? -ne 0 ]; then
    echo "ERROR: condor_submit not found in PATH"
    echo "You may need to load the Condor environment first."
    echo "Try running: module load condor"
    exit 1
fi

# Check condor status
echo "Checking condor status..."
condor_status
if [ $? -ne 0 ]; then
    echo "ERROR: condor_status failed. Condor may not be properly configured."
    exit 1
fi

# Check if we can submit a simple test job
echo "Creating a test job..."
TEST_DIR="condor_test"
mkdir -p $TEST_DIR

# Create a simple test script
cat > $TEST_DIR/test.sh << 'EOF'
#!/bin/bash
echo "Hello from Condor!"
hostname
date
EOF
chmod +x $TEST_DIR/test.sh

# Create a submit file
cat > $TEST_DIR/test.submit << 'EOF'
universe = vanilla
executable = test.sh
output = test.out
error = test.err
log = test.log
queue
EOF

# Try to submit the job
echo "Trying to submit a test job..."
cd $TEST_DIR
condor_submit test.submit
if [ $? -ne 0 ]; then
    echo "ERROR: Failed to submit test job."
    exit 1
fi

echo "Test job submitted successfully!"
echo "You can check its status with: condor_q"
echo "Once it completes, check the output with: cat $TEST_DIR/test.out"

echo "Condor environment check completed." 