#!/bin/bash

# This script checks the status of all condor jobs

condor_q | grep $(whoami)
