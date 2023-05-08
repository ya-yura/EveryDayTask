"""
TASK:
Given a real number n, find the square root of n.
Given an array of numbers and an index i, return the index of the nearest
larger number of the number at index i, where distance is measured
in array indices.

For example, given [4, 1, 3, 5, 6] and index 0, you should return 3.

If two distances to larger numbers are the equal, then return any one of them.
If the array at i doesn't have a nearest larger integer, then return null.

Follow-up: If you can preprocess the array, can you do this in constant time?
"""


def nearest_larger_number(nums, index):
    n = len(nums)
    nearest_right = [float('inf')] * n
    nearest_left = [float('inf')] * n

    # Find the nearest larger number on the right side
    stack = []
    for i in range(n - 1, index, -1):
        while stack and nums[i] >= nums[stack[-1]]:
            stack.pop()
        if stack:
            nearest_right[i] = stack[-1]
        stack.append(i)

    # Find the nearest larger number on the left side
    stack = []
    for i in range(index + 1):
        while stack and nums[i] >= nums[stack[-1]]:
            stack.pop()
        if stack:
            nearest_left[i] = stack[-1]
        stack.append(i)

    # Compare distances and return the index of the nearest larger number
    if (
        nearest_right[index] != float('inf')
        and nearest_left[index] != float('inf')
       ):
        if index - nearest_left[index] <= nearest_right[index] - index:
            return nearest_left[index]
        else:
            return nearest_right[index]
    elif nearest_right[index] != float('inf'):
        return nearest_right[index]
    elif nearest_left[index] != float('inf'):
        return nearest_left[index]
    else:
        return None

    """
    Algorithm description:

    To solve the given problem, we can use a two-pass approach.
    In the first pass, you can find the nearest larger number
    on the right side of each element, and in the second pass,
    find the nearest larger number on the left side.
    By comparing the distances from both sides, you can determine
    the index of the nearest larger number.
    """
