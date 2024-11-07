
data = {
    'money': [100, 150, 200, 250, 300, 350, 400, 450, 500, 550],
    'capitalAve': [50, 60, 70, 80, 90, 100, 110, 120, 130, 140],
    'capitalTotal': [500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400],
    'num857': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
}

# Create a DataFrame from the sample data
df = pd.DataFrame(data)

# Calculate the correlation matrix for all numeric features
correlation_matrix = df.corr()

# Mask the diagonal (correlation of a feature with itself is always 1)
import numpy as np
np.fill_diagonal(correlation_matrix.values, np.nan)

# Find the two features with the highest positive correlation
max_positive = correlation_matrix.stack().idxmax()  # This gives the pair with the highest positive correlation

# Find the two features with the highest negative correlation
min_negative = correlation_matrix.stack().idxmin()  # This gives the pair with the highest negative correlation

# Print the results
print(f"The two features with the highest positive correlation: {max_pos

