
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

# Create a heatmap of the correlation matrix
plt.figure(figsize=(8, 6))  # Optional: set the size of the plot
sns.heatmap(corr
