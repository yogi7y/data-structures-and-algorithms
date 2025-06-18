# G: 1.2
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


input = [1, 3, 2, 6, -1, 4, 1, 8, 2]
k = 5
expected_result = [2.2, 2.8, 2.4, 3.6, 2.8]

result = find_avg_of_contiguous_subarray_of_size_k(input, k)
assert result == expected_result

result_2 = find_avg_of_contiguous_subarray_of_size_k_2(input, k)
assert result_2 == expected_result
