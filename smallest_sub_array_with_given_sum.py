# G: 2.3
# Smallest subarray with given sum.

input_1 = [2, 1, 5, 2, 3, 2]
s_1 = 7
expected_1 = 2


input_2 = [2, 1, 5, 2, 8]
s_2 = 7
expected_2 = 1

input_3 = [3, 4, 1, 1, 6]
s_3 = 8
expected_3 = 3


def smallest_sub_array_with_given_sum(arr, s):
    start = end = sum = 0
    result = float("inf")

    while start <= end and end < len(arr):
        sum += arr[end]
        if sum < s:
            end += 1
        else:
            diff = (end - start) + 1
            result = min(diff, result)
            sum -= arr[start] + arr[end]
            start += 1

    return result


def smallest_sub_array_with_given_sum_2(arr, s):
    sum = start = 0
    min_length = float("inf")

    for end in range(len(arr)):
        sum += arr[end]

        while sum >= s:
            diff = end - start + 1
            min_length = min(diff, min_length)
            sum -= arr[start]
            start += 1

    if min_length == float("inf"):
        return 0

    return min_length


result_1 = smallest_sub_array_with_given_sum(input_1, s_1)
result_2 = smallest_sub_array_with_given_sum(input_2, s_2)
result_3 = smallest_sub_array_with_given_sum(input_3, s_3)

print(result_1)
print(result_2)
print(result_3)


assert result_1 == expected_1
assert result_2 == expected_2
assert result_3 == expected_3

result_2_1 = smallest_sub_array_with_given_sum_2(input_1, s_1)
result_2_2 = smallest_sub_array_with_given_sum_2(input_2, s_2)
result_2_3 = smallest_sub_array_with_given_sum_2(input_3, s_3)

print(result_2_1)
print(result_2_2)
print(result_2_3)


assert result_2_1 == expected_1
assert result_2_2 == expected_2
assert result_2_3 == expected_3
