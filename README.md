# dset-simulation
Data Security Energy Trading Simulation

### build images
In each folder, build the docker images to later import to GNS3.

/bin
/boot
/dev
/etc
/gns3
/gns3volumes
/home
/lib
/root
/sbin
/var
/usr


TTP: 
# DHCP config for eth0
auto eth0
iface eth0 inet dhcp
# Static config for eth1
auto eth1
iface eth1 inet static
	address 192.168.1.2
	netmask 255.255.255.0
	gateway 192.168.1.1


Node1:

# Static config for eth0
auto eth0
iface eth0 inet static
	address 192.168.1.3
	netmask 255.255.255.0
	gateway 192.168.1.1
#	up echo nameserver 192.168.1.1 > /etc/resolv.conf

# DHCP config for eth1
auto eth1
iface eth1 inet dhcp


Node 2:
