import matplotlib.pyplot as plt

ages = [12, 4, 10, 11, 15, 17, 18, 19, 22, 25, 29, 35, 37, 41, 45, 48, 52, 65, 69, 73, 80]

groups = {
    "Child (0-12)": 0,
    "Teenager (13-19)": 0,
    "Adult (20-39)": 0,
    "Senior (40+)": 0
}

for age in ages:
    if age <= 12:
        groups["Child (0-12)"] += 1
    elif 13 <= age <= 19:
        groups["Teenager (13-19)"] += 1
    elif 20 <= age <= 39:
        groups["Adult (20-39)"] += 1
    else:
        groups["Senior (40+)"] += 1

labels = list(groups.keys())
values = list(groups.values())

plt.figure(figsize=(8, 5))
plt.bar(labels, values, color="#EFA07A", edgecolor="gray", width=0.6)
plt.xlabel("Age Categories", fontsize=12)
plt.ylabel("Count", fontsize=12)
plt.title("Distribution of Age Groups", fontsize=14, fontweight='bold')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()
