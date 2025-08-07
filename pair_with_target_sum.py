# Given an array of sorted numbers and a target sum, find a pair in the array whose sum is equal to the given target.
# Write a function to return the indices of the two numbers (i.e. the pair) such that they add up to the given target.

cases = [
    {
        "input": [1, 2, 3, 4, 6],
        "target_sum": 6,
        "expected": [1, 3],
    },
    {
        "input": [2, 5, 9, 11],
        "target_sum": 11,
        "expected": [0, 2],
    },
]


def pair_with_target_sum(arr, target_sum):
    pass


for case in cases:
    result = pair_with_target_sum(case["input"], case["target_sum"])
    print(
        f"input: {case['input']}, target: {case['target_sum']}, expected: {case['expected']}, got: {result}"
    )
    assert result == case["expected"]
