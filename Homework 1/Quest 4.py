# Create a histogram for the 'money' feature using Seaborn
plt.figure(figsize=(10,6))  # Set the figure size
sns.histplot(df['money'], kde=False, color='blue', bins=30)  # kde=False means we are not showing the KDE curve
plt.title('Distribution of Money')  # Add title
plt.xlabel('Money Value')  # Label for the x-axis
plt.ylabel('Frequency')  # Label for the y-axis
plt.grid(True)  # Show grid
plt.show()
