# A single variable
company_name = "NBPO Sentinel"

# A list of integers (representing daily error counts)
daily_errors = [12, 4, 0, 15, 2]

print("System:", company_name)
print("Error Log:", daily_errors)
print("Data Type:", type(daily_errors))

# 1. Extracting data using Indexing
day_one_errors = daily_errors[0]
day_two_errors = daily_errors[1]

print(f"Day 1 Errors: {day_one_errors}")
print(f"Day 2 Errors: {day_two_errors}")

# 2. Extracting the LAST number in the list
print(daily_errors[-1])

# 3. Adding new data dynamically
print("Adding today's data...")
daily_errors.append(7)

print("Updated Error Log:", daily_errors)
# 4. Iterating through data to calculate an aggregate
total_errors = 0

print("--- Starting Error Calculation ---")

for count in daily_errors:
    # This block runs once for EVERY item in the list
    total_errors = total_errors + count
    print(f"Found {count} errors. Running total is now: {total_errors}")

print("----------------------------------")
print(f"Final Total Weekly Errors: {total_errors}")