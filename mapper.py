#!/usr/bin/env python3
import sys

for line in sys.stdin:
    data = line.strip().split("\t")
    if len(data) == 6:
        category = data[3]  # Assuming category is the 4th column (index 3)
        amount = float(data[4])
        print(f"{category}\t{amount}")
