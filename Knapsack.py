profits = [25, 24, 15]
weights = [18, 15, 10]
capacity = 20

n = len(profits)

memo = {}

def knapsack_top_down(i, capacity):
    if i == 0 or capacity == 0:
        return 0

    if (i, capacity) in memo:
        return memo[(i, capacity)]

    if weights[i - 1] <= capacity:
        take = profits[i - 1] + knapsack_top_down(
            i - 1, capacity - weights[i - 1]
        )
        skip = knapsack_top_down(i - 1, capacity)

        memo[(i, capacity)] = max(take, skip)
    else:
        memo[(i, capacity)] = knapsack_top_down(i - 1, capacity)

    return memo[(i, capacity)]


top_down_profit = knapsack_top_down(n, capacity)

dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

for i in range(1, n + 1):
    for w in range(1, capacity + 1):

        if weights[i - 1] <= w:
            dp[i][w] = max(
                profits[i - 1] + dp[i - 1][w - weights[i - 1]],
                dp[i - 1][w]
            )
        else:
            dp[i][w] = dp[i - 1][w]


bottom_up_profit = dp[n][capacity]

selected = []
w = capacity

for i in range(n, 0, -1):
    if dp[i][w] != dp[i - 1][w]:
        selected.append(i)
        w -= weights[i - 1]

selected.reverse()

print("TOP-DOWN (MEMOIZED)")
print("Maximum Profit:", top_down_profit)

print("\nBOTTOM-UP (TABULATION)")
print("Maximum Profit:", bottom_up_profit)

print("\nSelected Items:")
for i in selected:
    print("Item", i)

print("\nTotal Weight:",
      sum(weights[i - 1] for i in selected))

print("Total Profit:",
      sum(profits[i - 1] for i in selected))