
data = {
    'business': [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]  # Example data for 'business'
}

# Create a DataFrame from the sample data
df = pd.DataFrame(data)

# Calculate the 25th percentile (Q1) and 75th percentile (Q3)
Q1 = df['business'].quantile(0.25)
Q3 = df['business'].quantile(0.75)

# Calculate the Interquartile Range (IQR)
IQR = Q3 - Q1

# Print the results
print(f"25th Percentile (Q1) of 'business': {Q1}")
print(f"75th Percentile (Q3) of 'business': {Q3}")
print(f"Interquartile Range (IQR) of 'business': {IQR}")

