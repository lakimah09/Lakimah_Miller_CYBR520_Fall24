
data = {
    'table': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],  # Example data for 'table'
    'technology': [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]  # Example data for 'technology'
}

# Create a DataFrame from the sample data
df = pd.DataFrame(data)

# Calculate the Pearson correlation coefficient between 'table' and 'technology'
correlation = df['table'].corr(df['technology'])

# Print the result
print(f"The correlation coefficient between 'table' and 'technology' is: {correlation}")
