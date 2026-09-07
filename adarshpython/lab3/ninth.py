import numpy as np
import math
 
 
# ---------------------------------------------------------------------------
# 1. Datasets
# ---------------------------------------------------------------------------
marks = [78, 85, 92, 67, 88, 73, 95, 81, 76, 89]
temperatures = [28.5, 30.2, 29.8, 31.4, 27.9, 32.1, 30.5]
sales = [12500,13800,14200,11900,15100,14750,16000] 
 
# ---------------------------------------------------------------------------
# 2. Using NumPy
# ---------------------------------------------------------------------------
def stats_with_numpy(values):
    arr = np.array(values, dtype=float)
    return {
        "mean": np.mean(arr),
        "median": np.median(arr),
        "std_dev": np.std(arr),          # population std dev (ddof=0)
        "minimum": np.min(arr),
        "maximum": np.max(arr),
    }
 
 
# ---------------------------------------------------------------------------
# 3. Without NumPy (pure Python)
# ---------------------------------------------------------------------------
def mean_manual(values):
    return sum(values) / len(values)
 
 
def median_manual(values):
    sorted_vals = sorted(values)
    n = len(sorted_vals)
    mid = n // 2
    if n % 2 == 0:
        return (sorted_vals[mid - 1] + sorted_vals[mid]) / 2
    else:
        return sorted_vals[mid]
 
 
def std_dev_manual(values):
    m = mean_manual(values)
    variance = sum((x - m) ** 2 for x in values) / len(values)  # population variance
    return math.sqrt(variance)
 
 
def min_manual(values):
    smallest = values[0]
    for v in values:
        if v < smallest:
            smallest = v
    return smallest
 
 
def max_manual(values):
    largest = values[0]
    for v in values:
        if v > largest:
            largest = v
    return largest
 
 
def stats_without_numpy(values):
    return {
        "mean": mean_manual(values),
        "median": median_manual(values),
        "std_dev": std_dev_manual(values),
        "minimum": min_manual(values),
        "maximum": max_manual(values),
    }
 
 
# ---------------------------------------------------------------------------
# 4. Report
# ---------------------------------------------------------------------------
def print_report(label, data):
    np_stats = stats_with_numpy(data)
    manual_stats = stats_without_numpy(data)
 
    print(f"Dataset ({label}): {data}\n")
    header = f"{'Measure':<12}{'NumPy':>15}{'Pure Python':>15}"
    print(header)
    print("-" * len(header))
    for key in np_stats:
        print(f"{key:<12}{np_stats[key]:>15.4f}{manual_stats[key]:>15.4f}")
    print()
 
 
if __name__ == "__main__":
    print_report("marks", marks)
    print_report("temperatures", temperatures)
    print_report("sales",sales)
 
