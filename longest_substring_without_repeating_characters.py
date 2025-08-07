cases = [
    {
        "input": "aabccbb",
        "expected": 3,
    },
    {
        "input": "abbbb",
        "expected": 2,
    },
    {
        "input": "abccde",
        "expected": 3,
    },
]


def longest_substring_without_repeating_characters(input):
    max_length = 0

    for i in range(len(input)):
        first_char = input[i]
        occurred_chars = set()
        occurred_chars.add(first_char)

        for j in range(i + 1, len(input)):
            second_char = input[j]
            if second_char in occurred_chars:
                diff = j - i
                max_length = max(diff, max_length)
                break
            occurred_chars.add(second_char)

    return max_length


def longest_substring_without_repeating_characters_2(input):
    occurred_chars = dict()
    max_length = 0
    start = 0

    for end in range(len(input)):
        char = input[end]

        if char in occurred_chars:
            occurred_chars[char] += 1
        else:
            occurred_chars[char] = 1

        while occurred_chars[char] > 1:
            start_char = input[start]
            occurred_chars[start_char] -= 1
            if occurred_chars[start_char] == 0:
                del occurred_chars[start_char]
            start += 1

        diff = end - start + 1
        max_length = max(max_length, diff)

    return max_length


for case in cases:
    result = longest_substring_without_repeating_characters(case["input"])
    print(f"input: {case['input']}, expected: {case['expected']}, got: {result}")
    assert result == case["expected"]

    result_2 = longest_substring_without_repeating_characters_2(case["input"])
    print(f"input: {case['input']}, expected: {case['expected']}, got: {result_2}")
    assert result_2 == case["expected"]
