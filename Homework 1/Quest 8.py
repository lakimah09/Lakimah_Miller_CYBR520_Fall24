data = { 'esc': [130, 150, 180, 200, 220, 250, 300, 350, 400, 450] # dummy value for 'hp' }

Convert sample data to DataFrame
df = pd.DataFrame(data)

Determine the min / max of feature 'hp'
min_hp = df['hp'].min() max_hp = df['hp'].max()

Print the results
print("Minimum 'hp': {}".format(min_hp))

Output : Maximum 'hp' : max_hp