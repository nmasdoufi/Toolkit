#!/usr/bin/python3

import os

with open('ip-list.txt', 'w') as iplist:
    network_portion = '10.0.2'
    for i in range(1,255):
        iplist.writelines(network_portion + '.' + str(i) + '\n')

with open('ip-list.txt', 'r') as iplist:
    for line in iplist:
        line = line.rsplit() # strips whitespace
        # print(line[0])
        command = str(f'nc -nv -w 1 -z {line[0]} 80')
        os.system(command)

# BONUS :
# This same program can be done with a simple bash script:
# while read l; do nc -nv -w 1 -z $l 80; done <ip-list.txt