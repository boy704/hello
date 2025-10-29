data = {
    'Mango':  {'Yellow': 35, 'Sweet': 45, 'Long': 0,  'Total': 65},
    'Banana': {'Yellow': 40, 'Sweet': 30, 'Long': 35, 'Total': 40},
    'Orange': {'Yellow': 5,  'Sweet': 10, 'Long': 5,  'Total': 15}
}

total_yellow = 80
total_sweet = 85
total_long = 40
total_fruits = 120

features = ['Yellow', 'Sweet', 'Long']

results = {}

for fruit, values in data.items():
    prior = values['Total'] / total_fruits 
    likelihood = 1
    for feature in features:
        likelihood *= values[feature] / values['Total']  
    posterior = prior * likelihood
    results[fruit] = posterior

total_posterior = sum(results.values())
for fruit in results:
    results[fruit] /= total_posterior

print("Probabilities of Fruits:")
for fruit, prob in results.items():
    print(f"{fruit}: {prob:.2f}")

predicted_fruit = max(results, key=results.get)
print(f"\nPredicted Fruit: {predicted_fruit}")
