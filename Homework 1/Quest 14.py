
data = {
    'num857': [1, 5, 10, 20, 35, 40, 50, 60, 70, 80]  # Example data for 'num857'
}

# Create a DataFrame from the sample data
df = pd.DataFrame(data)

# Calculate the minimum and maximum values of 'num857'
min_value = df['num857'].min()
max_value = df['num857'].max()

# Calculate the range
range_value = max_value - min_value

# Print the results
print(f"Minimum value of 'num857': {min_value}")
print(f"Maximum value of 'num857': {max_value}")
print(f"Range of 'num857': {range_value}")

