#!/usr/bin/env sh
nvidia-smi | grep -A 3 Temp | tail -n 1 | awk '{print $3}'
