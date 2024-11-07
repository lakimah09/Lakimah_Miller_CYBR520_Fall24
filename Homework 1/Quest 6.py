spam_count = 1200 non_spam_count = 3800

Labels for the pie chart
labels = ['Spam', 'Non-Spam']

Data for the pie chart (number of spam and ham emails)
sizes = [spam_count, not_spam_count]

Slice colors (these colors can be customized)
colors = ['#ff9999','$66b3ff']

Create the pie chart
plt. plt.figure(figsize=(7, 7)) # only if we want the figure in specific size plt. Pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90, wedgeprops={'edgecolor':'black'})

Title of the pie chart
plt. title('Distribution of Emails Between Spam and Non-Spam types')
