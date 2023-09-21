##############################################################################
#   University of Washington Research Cruise
#   Aydin Karatas
###############################################################################
#!/bin/bash


cd "$(dirname "$0")" # this makes sure to run script in script's directory
clear
echo "Running calculations..."
python3 main.py data.txt
