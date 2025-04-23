def percent_improvement(baseline_stats, new_stats):
    """
    Calculates the percent improvement for mean, std, and max error values.
    Lower values are considered better.
    """
    improvement = {}
    for key in ("mean", "std", "max"):
        base = baseline_stats[key]
        new = new_stats[key]
        improvement[key] = 100.0 * (base - new) / abs(base)
    return improvement

# Example input values
baseline_stats = {
    "mean": 3.314567,
    "std": 2.647482,
    "max": 14.467972,
}

new_stats = {
    "mean": 2.197796,
    "std": 2.348706,
    "max": 34.888027,
}

# Compute improvements
improvement = percent_improvement(baseline_stats, new_stats)

# Display results
print(f"Mean Error Improvement: {improvement['mean']:+.2f}%")
print(f"Std  Error Improvement: {improvement['std']:+.2f}%")
print(f"Max  Error Improvement: {improvement['max']:+.2f}%")
