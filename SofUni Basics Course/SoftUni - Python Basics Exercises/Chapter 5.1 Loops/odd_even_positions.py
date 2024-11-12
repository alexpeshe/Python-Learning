n = int(input())

odd_sum = even_sum = 0
odd_min = even_min = float('inf')
odd_max = even_max = float('-inf')

for i in range(1, n + 1):
    num = float(input())
    if i % 2 == 0:  # even position
        even_sum += num
        even_min = min(even_min, num)
        even_max = max(even_max, num)
    else:  # odd position
        odd_sum += num
        odd_min = min(odd_min, num)
        odd_max = max(odd_max, num)

print(f"OddSum={odd_sum:.2f},")
print(f"OddMin={'No' if odd_min == float('inf') else odd_min:.2f},")
print(f"OddMax={'No' if odd_max == float('-inf') else odd_max:.2f},")
print(f"EvenSum={even_sum:.2f},")
print(f"EvenMin={'No' if even_min == float('inf') else even_min:.2f},")
print(f"EvenMax={'No' if even_max == float('-inf') else even_max:.2f}")