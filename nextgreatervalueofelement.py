"""
Program to find next greater value of every element and if no greater then -1 
"""
def next_larger_element(arr):
    n = len(arr)
    next_larger = [-1] * n
    stack = []
    for i in range(n-1, -1, -1):
        while stack and stack[-1] <= arr[i]:
            stack.pop()
        if stack:
            next_larger[i] = stack[-1]
        stack.append(arr[i])
    return next_larger

arr = [14, 2, 16, 4, 3, 5]
print(next_larger_element(arr))
#output [16, 16, -1, 5, 5, -1]
