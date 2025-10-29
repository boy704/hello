import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(0)
data = np.random.normal(loc=50, scale=10, size=100)
df = pd.DataFrame({'Value': data})

plt.figure(figsize=(10, 4))
plt.subplot(1, 2, 1)

plt.hist(df['Value'], bins=10, color='lightblue', edgecolor="black")
plt.title('Original Data Distribution')
plt.xlabel('Value')
plt.ylabel('Frequency')

df['Equal_Width_Bin'] = pd.cut(df['Value'], bins=4, labels=['Low', 'Medium', 'High', 'Very High'])
bin_counts = df['Equal_Width_Bin'].value_counts().sort_index()

plt.subplot(1, 2, 2)
plt.bar(bin_counts.index.astype(str), bin_counts.values, color='orange', edgecolor='black')
plt.title('Discretized Data (Equal-Width)')
plt.xlabel('Bins')
plt.ylabel('Count')

plt.tight_layout()
plt.show()

dataset = [
    ['<=30', 'High', 'No', 'Fair', 'No'],
    ['<=30', 'High', 'No', 'Excellent', 'No'],
    ['31-40', 'High', 'No', 'Fair', 'Yes'],
    ['>40', 'Medium', 'No', 'Fair', 'Yes'],
    ['>40', 'Low', 'Yes', 'Fair', 'Yes'],
    ['>40', 'Low', 'Yes', 'Excellent', 'No'],
    ['31-40', 'Low', 'Yes', 'Excellent', 'Yes'],
    ['<=30', 'Medium', 'No', 'Fair', 'No'],
    ['<=30', 'Low', 'Yes', 'Fair', 'Yes'],
    ['>40', 'Medium', 'Yes', 'Fair', 'Yes'],
    ['<=30', 'Medium', 'Yes', 'Excellent', 'Yes'],
    ['31-40', 'Medium', 'No', 'Fair', 'Yes'],
    ['31-40', 'High', 'Yes', 'Excellent', 'Yes'],
    ['>40', 'Medium', 'No', 'Excellent', 'No']
]

total = len(dataset)
yes_count = sum(1 for row in dataset if row[4] == 'Yes')
no_count = total - yes_count

P_yes = yes_count / total
P_no = no_count / total

def conditional_prob(attribute_index, attribute_value, target_class):
    count_attr_and_class = sum(
        1 for row in dataset if row[attribute_index] == attribute_value and row[4] == target_class
    )
    count_class = yes_count if target_class == 'Yes' else no_count
    return count_attr_and_class / count_class if count_class else 0

test = ['<=30', 'Medium', 'Yes', 'Fair']

P_x_given_yes = (
    conditional_prob(0, test[0], 'Yes') *
    conditional_prob(1, test[1], 'Yes') *
    conditional_prob(2, test[2], 'Yes') *
    conditional_prob(3, test[3], 'Yes')
)

P_x_given_no = (
    conditional_prob(0, test[0], 'No') *
    conditional_prob(1, test[1], 'No') *
    conditional_prob(2, test[2], 'No') *
    conditional_prob(3, test[3], 'No')
)

P_yes_given_x = P_x_given_yes * P_yes
P_no_given_x = P_x_given_no * P_no

if P_yes_given_x > P_no_given_x:
    result = "Buys Computer = Yes"
else:
    result = "Buys Computer = No"

print(f"P(Yes) = {round(P_yes, 3)}")
print(f"P(No) = {round(P_no, 3)}")
print(f"P(X|Yes) = {round(P_x_given_yes, 6)}")
print(f"P(X|No) = {round(P_x_given_no, 6)}")
print(f"P(Yes|X) = {round(P_yes_given_x, 6)}")
print(f"P(No|X) = {round(P_no_given_x, 6)}")
print(f"\nPredicted Class: {result}")