import sys

current_category = None
current_count = 0

for line in sys.stdin:
    category, _ = line.strip().split("\t")
    
    if current_category == category:
        current_count += 1
    else:
        if current_category:
            print(f"{current_category}\t{current_count}")
        current_category = category
        current_count = 1

if current_category == category:
    print(f"{current_category}\t{current_count}")
