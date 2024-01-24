import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime
import os
import time

def working_function(dat,tp):
    # Load the CSV file into a pandas DataFrame
    data = pd.read_csv(dat)

    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    output_folder = 'templates'
    # os.makedirs(output_folder, exist_ok=True)

    # Considering 'Close' prices for prediction
    prices = data['Close'].values.astype(float)

    def z_score_normalize(column):
        mean_val = column.mean()
        std_val = column.std()
        normalized_column = (column - mean_val) / std_val
        return normalized_column

    def min_max_normalize(column):
        min_val = column.min()
        max_val = column.max()
        normalized_column = (column - min_val) / (max_val - min_val)
        return normalized_column

    # Normalize the data
    prices_scaled = z_score_normalize(prices)

    # Define the sequence length for the RNN
    sequence_length = tp  # Adjust as needed

    # Prepare the data for training
    def prepare_data(prices_scaled, sequence_length):
        X = []
        for i in range(len(prices_scaled) - sequence_length):
            window = prices_scaled[i:(i + sequence_length)]
            X.append(window)
        return np.array(X)

    # Prepare sequences for the entire dataset
    X_full_data = prepare_data(prices_scaled, sequence_length)

    # Consider the last 3 days' data as the pattern to be searched
    pattern_to_search = X_full_data[-1]

    # Function to calculate similarity between sequences
    def calculate_similarity(seq1, seq2):
        return np.mean(np.abs(seq1 - seq2))

    # Search for similar patterns within the entire dataset
    matching_patterns = []


    for i, sequence in enumerate(X_full_data):  # Exclude the last 3 sequences for comparison
        similarity = calculate_similarity(pattern_to_search, sequence)
        if similarity >= 0.0 and similarity <= 0.3:
            matching_patterns.append((i, similarity,sequence))

    img_files = []
    # Print all matching patterns found
    if len(matching_patterns) > 0:
            fixed_pattern = pattern_to_search.flatten()
            print(f"Found {len(matching_patterns)} patterns in {len(X_full_data)} windows: of similarity level between 0.0 and 0.3")
            x,y = 0,0
            # Plot the fixed pattern
            for i in range(0,len(matching_patterns)-1):
                if matching_patterns[i+1][0] - matching_patterns[i][0] != 1: 
                    idx, similarity, sequence = matching_patterns[i-x]
                    print(f"Pattern found at index {idx} with similarity: {similarity:.4f},")
                    output_file = os.path.join(output_folder, f"graph_{timestamp}_{i}.png")
                    fig, axs = plt.subplots(1, 2, figsize=(10, 6))
                    axs[0].plot(fixed_pattern, label='Fixed Pattern')
                    axs[0].set_title('Fixed Pattern')
                    axs[0].legend()
                    # Plot the matching pattern
                    axs[1].plot(sequence.flatten(), label=f'Matching Pattern (Index {idx})')
                    axs[1].set_title(f'Matching Pattern (Similarity: {similarity:.4f})')
                    axs[1].legend()
                    plt.savefig(output_file)
                    plt.close()
                    # plt.tight_layout()
                    # plt.show()
                    y += 1
                    x = 0
                else:
                    x += 1
            print(f"Found {y} matching patterns in {len(X_full_data)} windows:")
    else:
        print("No matching patterns found.")

# working_function('D:/FInance Flash/application/csvdata/BAJAJHLDNG.csv', 360)
