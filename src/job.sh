#!/bin/bash
# Get the directory where the script is located
script_dir="$(dirname "$0")"

# Spark Submit
spark-submit $script_dir/main.py