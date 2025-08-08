"""
Problem Title: Longest Substring with K Distinct Characters
Difficulty: Medium
Tags: Sliding Window, HashMap, String Manipulation

Description:
Given a string, find the length of the longest substring that contains no more than K distinct characters.

Example 1:
Input: string="araaci", K=2
Output: 4
Explanation: The longest substring with no more than 2 distinct characters is "araa".

Example 2:
Input: string="araaci", K=1
Output: 2
Explanation: The longest substring with no more than 1 distinct character is "aa".

Example 3:
Input: string="cbbebi", K=3
Output: 5
Explanation: The longest substrings with no more than 3 distinct characters are "cbbeb" & "bbebi".
"""


def longest_substring_with_k_distinct(s: str, k: int) -> int:
    if k >= len(s):
        return len(s)

    frequency = dict()
    longest = 0
    window_start = 0

    for window_end in range(len(s)):
        character = s[window_end]

        if character not in frequency:
            frequency[character] = 1
        else:
            frequency[character] += 1

        while len(frequency) > k:
            start_character = s[window_start]
            if frequency[start_character] == 1:
                del frequency[start_character]
            else:
                frequency[start_character] -= 1
            window_start += 1

        length = (window_end - window_start) + 1
        longest = max(longest, length)

    return longest


# Test Cases
# Format: (input_tuple, expected_output, test_description)
test_cases = [
    (("araaci", 2), 4, "Basic case with normal input, K=2"),
    (("araaci", 1), 2, "Basic case with normal input, K=1"),
    (("cbbebi", 3), 5, "Basic case with normal input, K=3"),
    (("", 2), 0, "Edge case: empty string"),
    (("a", 1), 1, "Edge case: single character string with K=1"),
    (("abc", 3), 3, "Case where K equals the number of distinct characters"),
]


# Test Runner
def run_tests():
    print(f"Testing: {longest_substring_with_k_distinct.__name__}")

    passed = 0
    total = len(test_cases)

    for i, (args, expected, description) in enumerate(test_cases, 1):
        try:
            result = longest_substring_with_k_distinct(*args)
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
