import sys

current_category = None
current_sum = 0
current_count = 0

for line in sys.stdin:
    category, amount = line.strip().split("\t")
    amount = float(amount)
    
    if current_category == category:
        current_sum += amount
        current_count += 1
    else:
        if current_category:
            average = current_sum / current_count
            print(f"{current_category}\t{average}")
        current_category = category
        current_sum = amount
        current_count = 1

if current_category == category:
    average = current_sum / current_count
    print(f"{current_category}\t{average}")
