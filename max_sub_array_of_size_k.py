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

cases = [
    {
        "input": [2, 1, 5, 1, 3, 2],
        "k": 3,
        "expected": 9,
    },
    {
        "input": [2, 3, 4, 1, 5],
        "k": 2,
        "expected": 7,
    },
]

for case in cases:
    result = max_subarray_of_size_k(case["input"], case["k"])
    print(f"input: {case['input']}, k: {case['k']}, expected: {case['expected']}, got: {result}")
    assert result == case["expected"]
