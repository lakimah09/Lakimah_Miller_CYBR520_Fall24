
data = {
    'telnet': [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]  # Example data for 'telnet'
}

# Create a DataFrame from the sample data
df = pd.DataFrame(data)

# Calculate the 25th, 50th, and 75th percentiles for the 'telnet' column
percentile_25 = df['telnet'].quantile(0.25)
percentile_50 = df['telnet'].quantile(0.50)  # This is the median
percentile_75 = df['telnet'].quantile(0.75)

# Print the results
print(f"25th Percentile (Q1) of 'telnet': {percentile_25}")
print(f"50th Percentile (Median) of 'telnet': {percentile_50}")
print(f"75th Percentile (Q3) of 'telnet': {percentile_75}")

