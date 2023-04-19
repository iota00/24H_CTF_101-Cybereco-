#!/bin/bash

cat challenge | xxd -r -p | cut -d" " -f4| base64 -d > flag.txt
