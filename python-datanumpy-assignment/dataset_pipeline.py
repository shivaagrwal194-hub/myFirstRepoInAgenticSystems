import numpy as np

np.random.seed(42)

data = np.random.rand(100,3)

mean = np.mean(data, axis=0)
std = np.std(data, axis=0)

normalized = (data - mean) / std

train = normalized[ :80]
test = normalized[80: ]

print("Original data shape:", data.shape)
print("Mean shape:", mean.shape)
print("Training data shape:", train.shape)
print("Test data shape:", test.shape)

