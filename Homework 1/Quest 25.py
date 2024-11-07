
categories = ['Category A', 'Category B', 'Category C', 'Category D']
values = [40, 30, 20, 10]

# Create a pie chart
plt.figure(figsize=(7,7))  # Set the figure size for better display
plt.pie(values, labels=categories, autopct='%1.1f%%', startangle=140, colors=['#ff9999','#66b3ff','#99ff99','#ffcc99'])
plt.title('Category Distribution')
plt.show()
#advantages: comparisons are clear, easy to understand, appealing visually
#disadvantages: cluttered, no detail


