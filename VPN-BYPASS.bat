@ECHO OFF
netstat -r
route ADD 192.168.193.1 MASK 255.255.255.255 192.168.0.1
PAUSE