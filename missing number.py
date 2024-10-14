def find_missing_number(nums, n):
    # Sum of first n natural numbers
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(nums)
    # Missing number is the difference
    return expected_sum - actual_sum

# Example usage
nums = [1, 2, 4, 5, 6]  # Missing number is 3
n = 6  # Since numbers are from 1 to 6
missing_number = find_missing_number(nums, n)
print("Missing number:", missing_number)
