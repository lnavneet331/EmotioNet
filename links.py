import re

# Define the starting and ending series numbers
start_series = 201
end_series = 2790

# Create a set to store the found series numbers
found_series = set()

# Iterate through the lines of the text file
with open('links.txt', 'r') as file:
    for line in file:
        # Extract the series number using regular expressions
        match = re.search(r'N_(\d+)', line)
        if match:
            series_number = int(match.group(1))
            found_series.add(series_number)

# Check for missing series numbers
missing_series = []
for i in range(start_series, end_series + 1):
    if i not in found_series:
        missing_series.append(i)

# Print the missing series numbers
if missing_series:
    print("Missing series numbers:")
    for series_number in missing_series:
        print(f"N_{str(series_number).zfill(10)}")
else:
    print("No missing series numbers found.")
