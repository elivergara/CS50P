import matplotlib.pyplot as plt

# Caffeine content per serving (cup/shot)
caffeine_content = {
    "Brewed Coffee": 120,
    "Black Tea": 47,
    "Green Tea": 28,
    "Chai Tea": 50,  # Average value, can vary depending on black tea strength
    "Cafe Americano (Double Shot)": 180  # Assuming an average of 75mg per shot
}

# Sort data by caffeine content (high to low)
sorted_caffeine = dict(sorted(caffeine_content.items(), key=lambda item: item[1], reverse=True))

# Extract data for the table and graph
beverage_names = list(sorted_caffeine.keys())
beverage_caffeine = list(sorted_caffeine.values())

# Create a bar graph
plt.figure(figsize=(8, 6))
plt.bar(beverage_names, beverage_caffeine, color=['brown', 'skyblue', 'lightgreen', 'coral', 'yellowgreen'])
plt.xlabel("Beverage")
plt.ylabel("Caffeine (mg)")
plt.title("Caffeine Content Comparison (Sorted)")
plt.xticks(rotation=45, ha="right")  # Rotate x-axis labels for better readability
plt.tight_layout()
plt.show()