
# Create the histogram using Seaborn
sns.histplot(money_data, kde=True, color='blue', bins=30)

# Add labels and title
plt.title('Distribution of Money', fontsize=16)
plt.xlabel('Money', fontsize=14)
plt.ylabel('Frequency', fontsize=14)

# Show the plot
plt.show()

