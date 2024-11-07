
np.random.seed(0)
x = np.random.rand(50) * 100  # Advertising spend
y = 2 * x + 30 + np.random.randn(50) * 10  # Sales revenue with noise

# Create scatter plot
plt.scatter(x, y)
plt.xlabel('Advertising Spend')
plt.ylabel('Sales Revenue')
plt.title('Advertising Spend vs Sales Revenue')
plt.show()
