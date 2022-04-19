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
    
    net.addController('c0')

    h1 = net.addHost("h1", ip="10.0.0.1")
    h2 = net.addHost("h2", ip="10.0.0.2")
    h3 = net.addHost("h3", ip="10.0.0.3")
    h4 = net.addHost("h4", ip="10.0.0.4")
    h5 = net.addHost("h5", ip="10.0.0.5")
    h6 = net.addHost("h6", ip="10.0.0.6")
    h7 = net.addHost("h7", ip="10.0.0.7")
    h8 = net.addHost("h8", ip="10.0.0.8")


    s1 = net.addSwitch("s1")
    s2 = net.addSwitch("s2")
    s3 = net.addSwitch("s3")
    s4 = net.addSwitch("s4")
    s5 = net.addSwitch("s5")
    s6 = net.addSwitch("s6")
    s7 = net.addSwitch("s7")

    net.addLink("h1,s3")
    net.addLink("h2,s3")
    net.addLink("h3,s4")
    net.addLink("h4,s4")
    net.addLink("h5,s6")
    net.addLink("h6,s6")
    net.addLink("h7,s7")
    net.addLink("h8,s7")

    net.addLink("s3,s2")
    net.addLink("s4,s2")
    net.addLink("s6,s5")
    net.addLink("s7,s5")

    net.addLink("s2,s1")
    net.addLink("s5,s1")


    net.start()

    CLI(net)

    net.stop()









    
    

if __name__ == '__main__':
    setLogLevel( 'info' )
    treeTopo()
