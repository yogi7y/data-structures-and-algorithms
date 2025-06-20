# G: 2.4
# Longest substring with k distinct chars.

cases = [
    {
        "input": "araaci",
        "k": 2,
        "expected": 4,
    },
    {
        "input": "araaci",
        "k": 1,
        "expected": 2,
    },
    {
        "input": "cbbebi",
        "k": 3,
        "expected": 5,
    },
]


def longest_substring_with_distinct_chars(str, k):
    start = 0
    longest_substring = 0
    occurred_chars = dict()

    for end in range(len(str)):
        char = str[end]

        while len(occurred_chars) >= k and char not in occurred_chars:
            start_char = str[start]
            occurred_chars[start_char] -= 1
            if occurred_chars[start_char] == 0:
                occurred_chars.pop(start_char)
            start += 1

        if char in occurred_chars:
            occurred_chars[char] += 1
        else:
            occurred_chars[char] = 1

        diff = end - start + 1
        longest_substring = max(diff, longest_substring)

    return longest_substring


for case in cases:
    result = longest_substring_with_distinct_chars(case["input"], case["k"])
    print(result)
    assert result == case["expected"]
