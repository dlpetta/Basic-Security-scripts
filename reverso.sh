#!/bin/bash

for ip in $(seq 1 254);do
host -t ptr 37.59.174.$ip | grep -v "37.59.174" | cut -d " " -f 5 | grep -v "NXDOMAIN"

done
