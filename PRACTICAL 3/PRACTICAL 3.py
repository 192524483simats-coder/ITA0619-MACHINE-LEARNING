import math

data = [
    ['Sunny','Hot','No','No','No'],
    ['Sunny','Hot','Yes','No','No'],
    ['Overcast','Hot','No','Yes','Yes'],
    ['Rain','Mild','No','Yes','Yes'],
    ['Rain','Cool','No','Yes','Yes'],
    ['Rain','Cool','Yes','No','No'],
    ['Overcast','Cool','Yes','No','Yes'],
    ['Sunny','Mild','No','Yes','Yes']
]

def entropy(data):
    labels = [r[-1] for r in data]
    total = len(labels)
    e = 0

    for label in set(labels):
        p = labels.count(label) / total
        e -= p * math.log2(p)

    return e

def gain(data, col):
    total_entropy = entropy(data)
    values = set(r[col] for r in data)

    for v in values:
        subset = [r for r in data if r[col] == v]
        total_entropy -= (len(subset)/len(data)) * entropy(subset)

    return total_entropy

attributes = ['Outlook','Temperature','Humidity','Wind']

gains = [gain(data, i) for i in range(4)]
best = gains.index(max(gains))

print("Information Gain:")
for i in range(4):
    print(attributes[i], "=", round(gains[i], 3))

print("\nBest Attribute:", attributes[best])

# New sample
sample = ['Sunny','Mild','Yes','No']

if sample[2] == 'Yes':
    result = 'No'
else:
    result = 'Yes'

print("\nNew Sample:", sample)
print("Prediction:", result)
