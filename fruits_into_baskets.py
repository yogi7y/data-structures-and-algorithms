# G: 2.5
# Fruits into basket.

cases = [
    {
        "input": ["A", "B", "C", "A", "C"],
        "expected": 3,
    },
    {
        "input": ["A", "B", "C", "B", "B", "C"],
        "expected": 5,
    },
]


def fruits_into_basket(arr):
    k = 2
    basket = dict()
    start = 0

    for end in range(len(arr)):
        char = arr[end]

        if len(basket) >= k and char not in basket:
            start_char = arr[start]
            basket[start_char] -= 1
            if basket[start_char] <= 0:
                basket.pop(start_char)
            start += 1

        if char in basket:
            basket[char] += 1
        else:
            basket[char] = 1

    result = 0
    for value in basket.values():
        result += value

    return result


for case in cases:
    result = fruits_into_basket(case["input"])
    print(f"input: {case['input']}, expected: {case['expected']}, got: {result}")
    assert result == case["expected"]
