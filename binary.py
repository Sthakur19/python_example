def binary(n):
    binary_represntation = bin(n)[2:]

    current_gap = 0
    max_gap = 0
    for digit in binary_represntation:
        if digit == '0':
            current_gap += 1
        else:
            max_gap = max(max_gap, current_gap)
            current_gap = 0
    return max_gap

print(binary(1041))