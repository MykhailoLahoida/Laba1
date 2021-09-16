gold_bars = list(map(int, input("Enter the mass of gold bars in ascending order: ").split()))
capacity = int(input("Enter bag capacity: "))
result = 0
list_sum = [None]*len(gold_bars)
for i in range(len(gold_bars)):
    j = i
    while result <= capacity - gold_bars[j] and j < len(gold_bars):
        result = result + gold_bars[j]
        j = j+1
    list_sum[i] = result
    result = 0
max_number = max(list_sum)
print("Maximum weight of gold that fits into a knapsack with capacity of " + str(capacity) + " = " + str(max_number))
