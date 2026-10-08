import numpy as np

# Sigmoid function
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# Derivative of sigmoid
def sigmoid_derivative(x):
    return x * (1 - x)


# Training data (AND gate)
X = np.array([
    [0, 0],
    [0, 1],
    [1, 0],
    [1, 1]
])

# Target output
Y = np.array([
    [0],
    [0],
    [0],
    [1]
])


# Initialize weights and biases
np.random.seed(1)

W1 = np.random.uniform(-1, 1, (2, 3))
W2 = np.random.uniform(-1, 1, (3, 1))

b1 = np.zeros((1, 3))
b2 = np.zeros((1, 1))

# Learning rate
learning_rate = 0.5

# Number of training iterations
epochs = 10000


# Backpropagation training
for epoch in range(epochs):

    # ---------- Forward Propagation ----------
    hidden_input = np.dot(X, W1) + b1
    hidden_output = sigmoid(hidden_input)

    output_input = np.dot(hidden_output, W2) + b2
    output = sigmoid(output_input)

    # ---------- Calculate Error ----------
    error = Y - output

    # ---------- Backpropagation ----------
    output_delta = error * sigmoid_derivative(output)

    hidden_error = np.dot(output_delta, W2.T)
    hidden_delta = hidden_error * sigmoid_derivative(hidden_output)

    # ---------- Update Weights ----------
    W2 += np.dot(hidden_output.T, output_delta) * learning_rate
    b2 += np.sum(output_delta, axis=0, keepdims=True) * learning_rate

    W1 += np.dot(X.T, hidden_delta) * learning_rate
    b1 += np.sum(hidden_delta, axis=0, keepdims=True) * learning_rate


# ---------- Testing ----------
print("ANN using Backpropagation")
print("--------------------------")
print("Input\tActual\tPredicted")
print("--------------------------")

for i in range(len(X)):

    hidden = sigmoid(np.dot(X[i:i+1], W1) + b1)
    result = sigmoid(np.dot(hidden, W2) + b2)

    predicted = 1 if result[0][0] >= 0.5 else 0

    print(X[i], "\t", Y[i][0], "\t", predicted)
