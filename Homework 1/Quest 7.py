data = { our: [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000] # Sample data for the our feature }

Putting the sample data into DataFrame
df = pd.DataFrame(data)

Mean Median and Standard deviation
mean_value = df['our'].mean() median_value = df['our']. median() std_deviation = df['our']. std()

Print the results
print("Mean of 'our':", mean_value) print("Median of 'our': " + str(median_value)) print(f"'Our' Standard Deviation : {std_deviation}")