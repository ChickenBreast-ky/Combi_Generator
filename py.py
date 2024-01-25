from itertools import product

# Define the groups
A = ["교류전원", "직류전원", "배터리", "건전지", "해당없음"]
B = ["해당없음", "3세미만", "3세이상", "8세미만"]
C = ["해당없음", "국내", "해외"]
D = ["해당없음", "성인용"]

# Generate all possible combinations
combinations = list(product(A, B, C, D))

# Function to remove '해당없음' from a combination
def remove_irrelevant(combination):
    return tuple(item for item in combination if item != "해당없음")

# Apply the function to each combination and then filter out empty tuples
non_empty_combinations = [combo for combo in map(remove_irrelevant, combinations) if combo]

# Display the non-empty combinations
for combo in non_empty_combinations:
    print(combo)




