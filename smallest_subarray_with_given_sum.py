"""
Smallest Subarray with a Given Sum
Difficulty: Easy
Tags: Sliding Window, Arrays, Subarrays

Description:
Given an array of positive numbers and a positive number ‘S’,
find the length of the smallest contiguous subarray whose sum
is greater than or equal to ‘S’. Return 0 if no such subarray exists.

Examples:
Input: [2, 1, 5, 2, 3, 2], S=7
Output: 2
Explanation: The smallest subarray with a sum ≥ 7 is [5, 2]

Input: [2, 1, 5, 2, 8], S=7
Output: 1
Explanation: The smallest subarray with a sum ≥ 7 is [8]

Input: [3, 4, 1, 1, 6], S=8
Output: 3
Explanation: The smallest subarrays are [3, 4, 1] or [1, 1, 6]
"""


def smallest_subarray_with_given_sum(s: int, arr: list[int]) -> int:
    sum = 0
    start = 0
    min_length = float("inf")

    for end in range(len(arr)):
        sum += arr[end]
        print(f"start: {start}, end: {end}, sum: {sum}")

        while sum >= s:
            min_length = min(min_length, (end - start) + 1)
            print(f"setting min length to {min_length}")
            sum -= arr[start]
            start += 1

    return 0 if min_length == float("inf") else min_length


# Test Cases
# Format: (input_tuple, expected_output, test_description)
test_cases = [
    ((7, [2, 1, 5, 2, 3, 2]), 2, "Subarray [5, 2] meets sum 7 with length 2"),
    ((7, [2, 1, 5, 2, 8]), 1, "Subarray [8] meets sum 7 with length 1"),
    ((8, [3, 4, 1, 1, 6]), 3, "Multiple valid subarrays, smallest length is 3"),
    ((100, [1, 2, 3, 4, 5]), 0, "No subarray meets the sum"),
    ((4, [1, 4, 4]), 1, "Exact match with single elements"),
    ((3, [1, 1, 1, 1, 1, 1]), 3, "Sum only achieved with multiple small values"),
]


# Test Runner
def run_tests():
    print(f"Testing: {smallest_subarray_with_given_sum.__name__}")
    passed = 0
    total = len(test_cases)

    for i, (args, expected, description) in enumerate(test_cases, 1):
        try:
            result = smallest_subarray_with_given_sum(*args)
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
