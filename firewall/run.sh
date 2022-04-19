#!/bin/bash

# Note: Mininet must be run as root.  So invoke this shell script
# using sudo.

cd ~/pox
./pox.py forwarding.l2_learning


cd 
sudo ./sdn.py

pkill -9 pox.py

sudo mn -c
