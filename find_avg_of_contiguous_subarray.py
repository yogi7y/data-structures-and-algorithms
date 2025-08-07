# G: 2.1
# Given an array, find the average of all contiguous subarrays of size ‘K’ in it.


def find_avg_of_contiguous_subarray_of_size_k(arr, k):
    length = len(arr)
    output = []
    left = sum = 0

    for i in range(0, k):
        sum += arr[i]

    right = k - 1
    avg = sum / k

    output.append(avg)

    while right < length - 1:
        right += 1
        left += 1
        sum = sum - arr[left - 1] + arr[right]
        avg = sum / k
        output.append(avg)

    return output


def find_avg_of_contiguous_subarray_of_size_k_2(arr, k):
    start = sum = 0
    result = []

    for end in range(len(arr)):
        sum += arr[end]

        if end >= k - 1:
            avg = sum / k
            result.append(avg)
            sum -= arr[start]
            start += 1

    return result


cases = [
    {
        "input": [1, 3, 2, 6, -1, 4, 1, 8, 2],
        "k": 5,
        "expected": [2.2, 2.8, 2.4, 3.6, 2.8],
    },
]

for case in cases:
    result = find_avg_of_contiguous_subarray_of_size_k(case["input"], case["k"])
    print(
        f"input: {case['input']}, k: {case['k']}, expected: {case['expected']}, got: {result}"
    )
    assert result == case["expected"]

    result_2 = find_avg_of_contiguous_subarray_of_size_k_2(case["input"], case["k"])
    print(
        f"input: {case['input']}, k: {case['k']}, expected: {case['expected']}, got: {result_2}"
    )
    assert result_2 == case["expected"]
