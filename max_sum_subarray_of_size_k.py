"""
Maximum Sum Subarray of Size K
Difficulty: Easy
Tags: Sliding Window, Arrays, Subarrays

Description:
Given an array of positive numbers and a positive number k, find the maximum sum of any contiguous subarray of size ‘k’.

Examples:
Input: [2, 1, 5, 1, 3, 2], k=3
Output: 9
Explanation: Subarray with maximum sum is [5, 1, 3].

Input: [2, 3, 4, 1, 5], k=2
Output: 7
Explanation: Subarray with maximum sum is [3, 4].
"""


def max_sum_subarray_of_size_k(arr: list[int], k: int) -> int:
    sum = 0
    max_sum = 0
    start = 0

    for end in range(len(arr)):
        current_number = arr[end]
        sum += current_number

        if end >= k - 1:
            max_sum = max(max_sum, sum)
            sum -= arr[start]
            start += 1

    return max_sum


# Test Cases
# Format: (input_tuple, expected_output, test_description)
test_cases = [
    (([2, 1, 5, 1, 3, 2], 3), 9, "Basic case with max sum subarray [5,1,3]"),
    (([2, 3, 4, 1, 5], 2), 7, "Simple case with subarray [3,4]"),
    (([1, 1, 1, 1, 1], 2), 2, "All elements same"),
    (([5], 1), 5, "Single element array with k=1"),
    (([1, 2, 3, 4, 5], 5), 15, "Subarray equals full array"),
    (([5, 2, 1, 6, 3, 4, 7], 4), 20, "Larger array with clear max window [6,3,4,7]"),
]


# Test Runner
def run_tests():
    print(f"Testing: {max_sum_subarray_of_size_k.__name__}")
    passed = 0
    total = len(test_cases)

    for i, (args, expected, description) in enumerate(test_cases, 1):
        try:
            result = max_sum_subarray_of_size_k(*args)
            status = "PASS" if result == expected else "FAIL"

            print(f"Test {i}: {status}")
            print(f"  Description: {description}")
            print(f"  Input: {args}")
            print(f"  Expected: {expected}")
            print(f"  Got: {result}")
            print()

            if status == "PASS":
                passed += 1

        except Exception as e:
            print(f"Test {i}: ERROR")
            print(f"  Description: {description}")
            print(f"  Input: {args}")
            print(f"  Error: {e}")
            print()

    print(f"Results: {passed}/{total} tests passed")
    return passed == total


if __name__ == "__main__":
    run_tests()
