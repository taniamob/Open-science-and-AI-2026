#!/bin/bash
set -e

echo "Starting analysis codes......."


python code/extract_abs.py
python code/keyword_cloud.py
python code/num_fig.py
python code/links.py

echo "All codes are done"