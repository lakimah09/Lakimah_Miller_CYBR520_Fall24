
data = {
    'num3d': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],  # Example data for 'num3d'
    'num000': [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]  # Example data for 'num000'
}

# Create a DataFrame from the sample data
df = pd.DataFrame(data)

# Calculate the Pearson correlation coefficient between 'num3d' and 'num000'
correlation = df['num3d'].corr(df['num000'])

# Print the result
print(f"The correlation coefficient between 'num3d' and 'num000' is: {correlation}")

