import math

class NaiveBayesClassifier:
    def __init__(self):
        self.priors = {}
        self.likelihoods = {}
        self.class_counts = {}
        self.feature_value_counts = {}
        self.features = []
        self.target_name = ""
        self.target_values = []

    def fit(self, data, features, target_name):
        self.features = features
        self.target_name = target_name
        n_rows = len(data)

        self.target_values = sorted(list(set([row[-1] for row in data])))
        
        data_by_class = {class_val: [] for class_val in self.target_values}
        for row in data:
            class_val = row[-1]
            data_by_class[class_val].append(row)

        print("--- Training Started ---")
        print(f"Total instances: {n_rows}")
        
        for class_val in self.target_values:
            class_rows = data_by_class[class_val]
            n_class_rows = len(class_rows)
            
            self.class_counts[class_val] = n_class_rows
            
            self.priors[class_val] = n_class_rows / n_rows
            
            print(f"Class '{class_val}': {n_class_rows} instances. Prior P({class_val}) = {self.priors[class_val]:.3f}")
            
            self.likelihoods[class_val] = {}
        print("\nCalculating Likelihoods (with Laplace Smoothing)...")
        
        for i, feature_name in enumerate(self.features):
            all_vals_for_feature = sorted(list(set([row[i] for row in data])))
            
            k = len(all_vals_for_feature)
            self.feature_value_counts[feature_name] = k
            print(f"  Feature '{feature_name}' (k={k}):")

            for class_val in self.target_values:
                if feature_name not in self.likelihoods[class_val]:
                    self.likelihoods[class_val][feature_name] = {}
                
                class_rows = data_by_class[class_val]
                n_class_rows = len(class_rows)
                
                feature_vals_in_class = [row[i] for row in class_rows]
                
                for value in all_vals_for_feature:
                    count = feature_vals_in_class.count(value)
                    
                    probability = (count + 1) / (n_class_rows + k)
                    
                    self.likelihoods[class_val][feature_name][value] = probability
                    print(f"    P({feature_name}={value} | {class_val}) = ({count}+1) / ({n_class_rows}+{k}) = {probability:.3f}")

        print("--- Training Complete ---")


    def predict(self, instance):
        if not self.priors:
            raise ValueError("Classifier has not been trained. Call fit() first.")
            
        log_probabilities = {}
        
        for class_val in self.target_values:
            log_prob = math.log(self.priors[class_val])
            
            for i, feature_name in enumerate(self.features):
                value = instance[i]
                
                if value in self.likelihoods[class_val][feature_name]:
                    log_prob += math.log(self.likelihoods[class_val][feature_name][value])
                else:
                    k = self.feature_value_counts[feature_name]
                    n_class_rows = self.class_counts[class_val]
                    smoothed_prob = (0 + 1) / (n_class_rows + k)
                    log_prob += math.log(smoothed_prob)
                    
                    print(f"Warning: Value '{value}' for feature '{feature_name}' was not in training data. Applying smoothing.")
            
            log_probabilities[class_val] = log_prob
            
        max_log_prob = max(log_probabilities.values())
        
        relative_probs = {}
        total_prob = 0.0
        for class_val, log_prob in log_probabilities.items():
            relative_probs[class_val] = math.exp(log_prob - max_log_prob)
            total_prob += relative_probs[class_val]
            
        final_probabilities = {class_val: (prob / total_prob) for class_val, prob in relative_probs.items()}

        predicted_class = max(log_probabilities, key=log_probabilities.get)
        
        return predicted_class, final_probabilities


def get_valid_input(prompt_text, valid_options_lower):
    mapping = {
        'sunny': 'Sunny', 'overcast': 'Overcast', 'rain': 'Rain',
        'hot': 'Hot', 'mild': 'Mild', 'cool': 'Cool',
        'high': 'High', 'normal': 'Normal',
        'weak': 'Weak', 'strong': 'Strong'
    }

    while True:
        user_input = input(prompt_text).strip().lower()
        
        if user_input in valid_options_lower:
            return mapping[user_input]
        else:
            print(f"Invalid input. Please enter one of: {', '.join(valid_options_lower)}")

if __name__ == "__main__":
    data = [
        ['Sunny', 'Hot', 'High', 'Weak', 'No'],
        ['Sunny', 'Hot', 'High', 'Strong', 'No'],
        ['Overcast', 'Hot', 'High', 'Weak', 'Yes'],
        ['Rain', 'Mild', 'High', 'Weak', 'Yes'],
        ['Rain', 'Cool', 'Normal', 'Weak', 'Yes'],
        ['Rain', 'Cool', 'Normal', 'Strong', 'No'],
        ['Overcast', 'Cool', 'Normal', 'Strong', 'Yes'],
        ['Sunny', 'Mild', 'High', 'Weak', 'No'],
        ['Sunny', 'Cool', 'Normal', 'Weak', 'Yes'],
        ['Rain', 'Mild', 'Normal', 'Weak', 'Yes'],
        ['Sunny', 'Mild', 'Normal', 'Strong', 'Yes'],
        ['Overcast', 'Mild', 'High', 'Strong', 'Yes'],
        ['Overcast', 'Hot', 'Normal', 'Weak', 'Yes'],
        ['Rain', 'Mild', 'High', 'Strong', 'No']
    ]
    
    features = ['Outlook', 'Temperature', 'Humidity', 'Wind']
    target = 'PlayTennis'
    
    nb_classifier = NaiveBayesClassifier()
    nb_classifier.fit(data, features, target)
    
    print("\n--- Enter Weather Conditions for Prediction ---")
    
    outlook = get_valid_input(
        "Enter Outlook (sunny, overcast, rain): ", 
        ['sunny', 'overcast', 'rain']
    )
    temperature = get_valid_input(
        "Enter Temperature (hot, mild, cool): ", 
        ['hot', 'mild', 'cool']
    ) 
    humidity = get_valid_input(
        "Enter Humidity (high, normal): ", 
        ['high', 'normal']
    )
    wind = get_valid_input(
        "Enter Wind (weak, strong): ", 
        ['weak', 'strong']
    )
    new_instance = [outlook, temperature, humidity, wind]
    
    print(f"\n--- Making Prediction for: {list(zip(features, new_instance))} ---")
    
    prediction, probabilities = nb_classifier.predict(new_instance)
    
    print(f"\nPredicted Class: {prediction}")
    print("Class Probabilities:")
    for class_val, prob in probabilities.items():
        print(f"  P({class_val}): {prob:.4f} ({prob*100:.2f}%)")