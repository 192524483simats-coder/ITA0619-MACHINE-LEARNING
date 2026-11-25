# FIND-S Algorithm

data = [
    ['Sunny', 'Warm', 'Normal', 'Strong', 'Warm', 'Same', 'Yes'],
    ['Sunny', 'Warm', 'High', 'Strong', 'Warm', 'Same', 'Yes'],
    ['Rainy', 'Cold', 'High', 'Strong', 'Warm', 'Change', 'No'],
    ['Sunny', 'Warm', 'High', 'Strong', 'Cool', 'Change', 'Yes']
]

# Initialize hypothesis with first positive example
h = data[0][:-1]

# Find-S
for row in data:
    if row[-1] == 'Yes':
        for i in range(len(h)):
            if h[i] != row[i]:
                h[i] = '?'

print("Most Specific Hypothesis:")
print(h)
