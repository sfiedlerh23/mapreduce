import sys

allowed_categories = {"Computers", "Cameras", "Video Games"}

for line in sys.stdin:
    data = line.strip().split("\t")
    if len(data) == 6:
        category = data[3]
        amount = float(data[4])
        if category in allowed_categories:
            print(f"{category}\t{amount}")
