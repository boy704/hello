from itertools import combinations
from collections import defaultdict

transactions = [
    {'i1', 'i2', 'i3'},
    {'i1', 'i2', 'i4'},
    {'i1', 'i2', 'i3', 'i4'},
    {'i1', 'i3', 'i5'},
    {'i1', 'i2', 'i3', 'i4'}
]

min_support_percent = 50
min_confidence = 0.6

def get_support_count(itemset, transactions):
    return sum(1 for transaction in transactions if itemset.issubset(transaction))

def filter_items_by_support(transactions, min_support_count):
    item_counts = defaultdict(int)
    for transaction in transactions:
        for item in transaction:
            item_counts[item] += 1

    frequent_items = {item for item, count in item_counts.items() if count >= min_support_count}
    filtered_transactions = [
        {item for item in transaction if item in frequent_items}
        for transaction in transactions
    ]
    return filtered_transactions

def get_frequent_itemsets(transactions, min_support_count):
    freq_itemsets = dict()
    single_items = set(item for transaction in transactions for item in transaction)
    current_itemsets = [frozenset([item]) for item in single_items]
    k = 1

    while current_itemsets:
        freq_k_itemsets = dict()
        for itemset in current_itemsets:
            support_count = get_support_count(itemset, transactions)
            if support_count >= min_support_count:
                freq_k_itemsets[itemset] = support_count

        freq_itemsets.update(freq_k_itemsets)
        next_itemsets = set()
        keys = list(freq_k_itemsets.keys())

        for i in range(len(keys)):
            for j in range(i + 1, len(keys)):
                union = keys[i] | keys[j]
                if len(union) == k + 1:
                    next_itemsets.add(union)

        current_itemsets = list(next_itemsets)
        k += 1

    return freq_itemsets

def generate_association_rules_for_itemset(itemset, transactions, min_confidence):
    rules = []
    for i in range(1, len(itemset)):
        for antecedent in combinations(itemset, i):
            antecedent = frozenset(antecedent)
            consequent = itemset - antecedent
            antecedent_support = get_support_count(antecedent, transactions)
            itemset_support = get_support_count(itemset, transactions)
            confidence = itemset_support / antecedent_support
            if confidence >= min_confidence:
                rules.append((antecedent, consequent, confidence))
    return rules

num_transactions = len(transactions)
min_support_count = (min_support_percent / 100) * num_transactions

filtered_transactions = filter_items_by_support(transactions, min_support_count)
frequent_itemsets = get_frequent_itemsets(filtered_transactions, min_support_count)

print("\nFiltered Transactions:")
for i, t in enumerate(filtered_transactions, start=1):
    print(f"T{i}: {t}")

print("\nFrequent Itemsets:")
for itemset, count in sorted(frequent_itemsets.items(), key=lambda x: (len(x[0]), sorted(x[0]))):
    print(f"{set(itemset)} : support = {count}")

frequent_3_itemsets = sorted(
    [itemset for itemset in frequent_itemsets if len(itemset) == 3],
    key=lambda x: sorted(x)
)

if frequent_3_itemsets:
    last_3_itemset = frequent_3_itemsets[-1]
    support = get_support_count(last_3_itemset, filtered_transactions)
    rules = generate_association_rules_for_itemset(last_3_itemset, filtered_transactions, min_confidence)

    print(f"\nLast Frequent 3-Itemset: {set(last_3_itemset)}")
    print(f"Support Count: {support}")

    print(f"\nAssociation Rules (min confidence {min_confidence * 100}%):")
    for antecedent, consequent, confidence in rules:
        print(f"{set(antecedent)} => {set(consequent)} (confidence = {confidence:.2f})")

else:
    print("\nNo frequent 3-item itemsets found.")
