#!/bin/bash

# Default number of ellipsoids to view
DEFAULT_NUM_ELLIPSOIDS=25

# Get number of ellipsoids from command line argument, or use default
num_ellipsoids=${1:-$DEFAULT_NUM_ELLIPSOIDS}

echo "Viewing $num_ellipsoids ellipsoids..."

blender --background --python view.py -- $num_ellipsoids 1> view_txt
rm -rf view_txt