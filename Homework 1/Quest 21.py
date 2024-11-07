
data = {
    'font': [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],  # Example data for 'font'
    'money': [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]  # Example data for 'money'
}

# Create a DataFrame from the sample data
df = pd.DataFrame(data)

# Calculate the Pearson correlation coefficient between 'font' and 'money'
correlation = df['font'].corr(df['money'])

# Print the result
print(f"The correlation coefficient between 'font' and 'money' is: {correlation}")
