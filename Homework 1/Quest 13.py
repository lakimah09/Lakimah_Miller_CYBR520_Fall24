
data = {
    'capitalAve': [100, 150, 200, 250, 300, 350, 400, 450, 500, 550],  # Example data for 'capitalAve'
    'capitalTotal': [1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500, 5000, 5500]  # Example data for 'capitalTotal'
}

# Create a DataFrame from the sample data
df = pd.DataFrame(data)

# Calculate the correlation coefficient between 'capitalAve' and 'capitalTotal'
correlation = df['capitalAve'].corr(df['capitalTotal'])

# Print the result
print(f"The correlation coefficient between 'capitalAve' and 'capitalTotal' is: {correlation}")

