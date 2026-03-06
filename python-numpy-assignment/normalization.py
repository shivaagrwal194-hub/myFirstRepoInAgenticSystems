import numpy as np

# Step 1: Create NumPy array
data = np.array([10, 20, 30, 40])

# Step 2: Compute mean and standard deviation
mean = np.mean(data)
std = np.std(data)

# Step 3: Normalize the data
normalized = (data - mean) / std

# Step 4: Reshape into 2D array
reshaped = normalized.reshape(2, 2)

# Step 5: Print results
print("Original data:", data)
print("Mean:", mean)
print("Standard Deviation:", round(std, 2))
print("Normalized data:", np.round(normalized, 2))
print("Reshaped data:\n", np.round(reshaped, 2))
print("Reshaped data shape:", reshaped.shape)