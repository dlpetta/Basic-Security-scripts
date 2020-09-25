#!/bin/bash

for ip in $(seq 1 254);do
host -t ptr 132.148.90.$ip | grep -v "132.148.90" | cut -d " " -f 5 | grep -v "NXDOMAIN"

done
