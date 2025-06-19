# G: 2.2
# Find the maximum sum of any contiguous subarray of size ‘k’.


def max_subarray_of_size_k(arr, k):
    start = sum = result = 0

    for end in range(len(arr)):
        sum += arr[end]
        diff = end - start + 1

        if diff >= k:
            result = max(result, sum)
            sum -= arr[start]
            start += 1

    return result


input_1 = [2, 1, 5, 1, 3, 2]
k_1 = 3
expected_1 = 9

input_2 = [2, 3, 4, 1, 5]
k_2 = 2
expected_2 = 7

result_1 = max_subarray_of_size_k(input_1, k_1)
result_2 = max_subarray_of_size_k(input_2, k_2)

assert result_1 == expected_1
assert result_2 == expected_2
