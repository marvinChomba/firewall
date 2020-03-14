#!/usr/bin/python

# EEE4121F-B Lab 2
# SDN

# Implementing a Layer-2 Firewall using POX and Mininet


from mininet.net import Mininet
from mininet.node import RemoteController
from mininet.cli import CLI
from mininet.log import setLogLevel, info

def treeTopo():
    net = Mininet( controller=RemoteController )
    
    

if __name__ == '__main__':
    setLogLevel( 'info' )
    treeTopo()
