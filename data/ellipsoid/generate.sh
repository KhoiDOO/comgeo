#!/bin/bash

# Default number of ellipsoids to generate
DEFAULT_NUM_ELLIPSOIDS=60000

# Get number of ellipsoids from command line argument, or use default
num_ellipsoids=${1:-$DEFAULT_NUM_ELLIPSOIDS}

echo "Generating $num_ellipsoids ellipsoids..."

blender --background --python generate.py -- $num_ellipsoids 1> generate.txt
rm -rf generate.txt