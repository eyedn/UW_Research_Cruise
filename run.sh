##############################################################################
#   University of Washington Research Cruise
#   Aydin Karatas
###############################################################################
#!/bin/bash


cd "$(dirname "$0")" # this makes sure the run script is ran in its directory
echo "Running calculations..."
python3 main.py data.txt
