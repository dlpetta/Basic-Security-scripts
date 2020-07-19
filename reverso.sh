#!/bin/bash

for ip in $(seq 1 254);do
host -t ptr $1.$ip | grep -v "NXDOMAIN" | grep -v $1
done
