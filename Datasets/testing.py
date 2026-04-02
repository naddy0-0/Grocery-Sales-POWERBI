# Five-number summary, range, IQR, outliers, and boxplot
import numpy as np
import matplotlib.pyplot as plt

# Data
scores = np.array([25, 45, 71, 75, 76, 77, 78, 79, 81, 83,
                   85, 86, 87, 90, 91, 92, 95, 95, 99, 100])

# Sort (already sorted but ensure)
scores = np.sort(scores)

# Five-number summary
minimum = np.min(scores)
q1 = np.percentile(scores, 25, interpolation='midpoint')
median = np.percentile(scores, 50, interpolation='midpoint')
q3 = np.percentile(scores, 75, interpolation='midpoint')
maximum = np.max(scores)

# Range and IQR
_range = maximum - minimum
iqr = q3 - q1

# Outlier fences
lower_fence = q1 - 1.5 * iqr
upper_fence = q3 + 1.5 * iqr

# Identify outliers
outliers = scores[(scores < lower_fence) | (scores > upper_fence)]
non_outlier_min = np.min(scores[scores >= lower_fence]) if np.any(scores >= lower_fence) else minimum
non_outlier_max = np.max(scores[scores <= upper_fence]) if np.any(scores <= upper_fence) else maximum

# Print results
print("Five-number summary:")
print(f"Minimum: {minimum}")
print(f"Q1: {q1}")
print(f"Median: {median}")
print(f"Q3: {q3}")
print(f"Maximum: {maximum}")
print()
print(f"Range: {_range}")
print(f"IQR: {iqr}")
print()
print(f"Lower fence (Q1 - 1.5*IQR): {lower_fence}")
print(f"Upper fence (Q3 + 1.5*IQR): {upper_fence}")
print()
print("Outliers:", outliers.tolist())
print(f"Whisker lower end (smallest non-outlier): {non_outlier_min}")
print(f"Whisker upper end (largest non-outlier): {non_outlier_max}")

# Boxplot
plt.figure(figsize=(8, 4))
plt.boxplot(scores, vert=False, showmeans=True, widths=0.6,
            flierprops=dict(marker='o', markerfacecolor='red', markersize=6))
plt.yticks([1], ['Test Scores'])
plt.title('Box-and-Whisker Plot of Test Scores')
plt.xlabel('Score')
plt.grid(axis='x', linestyle='--', alpha=0.5)
plt.show()
