def min_total_bonus(rates):
    n = len(rates)
    bonuses = [500] * n

    # Iterate from left to right to update bonuses
    for i in range(1, n):
        if rates[i] > rates[i - 1]:
            bonuses[i] = max(bonuses[i], bonuses[i - 1] + 500)

    # Iterate from right to left to update bonuses
    for i in range(n - 2, -1, -1):
        if rates[i] > rates[i + 1]:
            bonuses[i] = max(bonuses[i], bonuses[i + 1] + 500)

    return sum(bonuses)

# Example usage:
rates = [100, 200, 150, 250, 300]
print("Minimum sum of bonuses:", min_total_bonus(rates))
