import csv

# Read training data from Downloads
with open(r"C:\Users\Hp\Downloads\trainingdata.csv", "r") as f:
    data = list(csv.reader(f))

attributes = data[0][:-1]
examples = data[1:]

n = len(attributes)

# Initialize Specific and General boundaries
S = ['0'] * n
G = [['?'] * n]

# Candidate Elimination Algorithm
for example in examples:

    x = example[:-1]
    label = example[-1]

    # Positive example
    if label == "Yes":

        # Remove hypotheses from G that do not cover x
        G = [
            g for g in G
            if all(g[i] == '?' or g[i] == x[i] for i in range(n))
        ]

        # Generalize S
        for i in range(n):
            if S[i] == '0':
                S[i] = x[i]

            elif S[i] != x[i]:
                S[i] = '?'

    # Negative example
    else:

        # Specialize G
        new_G = []

        for g in G:
            for i in range(n):

                if g[i] == '?' and S[i] != '?' and S[i] != x[i]:
                    new_g = g.copy()
                    new_g[i] = S[i]

                    if new_g not in new_G:
                        new_G.append(new_g)

        G = new_G


# Display results
print("Specific Boundary (S):")
print(S)

print("\nGeneral Boundary (G):")

for g in G:
    print(g)
