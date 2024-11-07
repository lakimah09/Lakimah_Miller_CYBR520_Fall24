import pandas as pd


data = {
    'you': ['yes', 'no', 'yes', 'yes', 'no', 'no', 'yes', 'maybe', 'no', 'yes']  # Example data for 'you'
}

# Create a DataFrame from the sample data
df = pd.DataFrame(data)

# Find the mode of the 'you' column
mode_value = df['you'].mode()[0]  # mode() returns a Series, so we take the first element

# Print the result
print(f"The mode of the 'you' feature is: {mode_value}")

