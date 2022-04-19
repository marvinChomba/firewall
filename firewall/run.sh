#!/bin/bash

# Note: Mininet must be run as root.  So invoke this shell script
# using sudo.

#redirecting output

sudo ./sdn.py

pkill -9 pox.py

sudo mn -c