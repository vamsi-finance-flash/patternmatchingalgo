import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics.pairwise import cosine_similarity
import tensorflow as tf

# Function to normalize data
# Function to normalize data
def min_max_normalize(column):
    min_val = column.min()
    max_val = column.max()
    normalized_column = (column - min_val) / (max_val - min_val)
    return normalized_column

# Load and normalize data
dat = 'D:/FInance Flash/application/csvdata/BAJAJHLDNG.csv'
data = pd.read_csv(dat)
close_data = data["Close"]
normalized_data = min_max_normalize(close_data)

# Define input pattern
window_size = 50  # Adjust as needed
input_pattern = normalized_data[-window_size:].values.reshape(-1, 1)  # Select the last "window_size" values for the pattern

# Function to find similar patterns using RNN
def find_similar_patterns_rnn(pattern, data, threshold=0.9):
    # RNN architecture and training
    model = tf.keras.Sequential([
        tf.keras.layers.SimpleRNN(units=32, activation='relu', input_shape=(window_size, 1)),
        tf.keras.layers.Dense(1)
    ])

    # Data preprocessing
    x_train = []
    y_train = []
    for i in range(len(data) - window_size):
        x_train.append(data[i:i+window_size])
        y_train.append(data[i+window_size])
    x_train = np.array(x_train).reshape(-1, window_size, 1)
    y_train = np.array(y_train).reshape(-1, 1)

    model.compile(optimizer='adam', loss='mean_squared_error')
    model.fit(x_train, y_train, epochs=10, verbose=0)  # Adjust epochs as needed

    # Generate predictions for each subsequence
    predictions = []
    for i in range(len(data) - len(pattern) + 1):
        subsequence = data[i:i+len(pattern)]
        prediction = model.predict(subsequence.values.reshape(1, -1, 1))[0, -1]
        predictions.append(prediction)

    # Calculate similarity scores and find similar patterns
    similarity_scores = cosine_similarity([input_pattern.flatten()], predictions)[0]

    similar_indices = np.where(similarity_scores >= threshold)[0]

    similar_patterns = []
    for index in similar_indices:
        start_time = data.index[index]
        end_time = data.index[index + len(pattern) - 1]
        pattern = data[index:index+len(pattern)]
        similar_patterns.append((start_time, end_time, pattern))

    return similar_patterns

# Find similar patterns using the RNN
similar_patterns = find_similar_patterns_rnn(input_pattern, normalized_data)

# Visualize similar patterns
for start_time, end_time, pattern in similar_patterns:
    plt.figure(figsize=(12, 6))
    plt.plot(normalized_data, label="Normalized Close Prices")
    plt.plot(pattern.index, pattern.values, label="Similar Pattern")
    plt.xlim(start_time, end_time)
    # plt.title(f"Similar Pattern Found (Similarity: {similarity:.2f})")
    plt.legend()
    plt.show()
