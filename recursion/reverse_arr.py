class Solution:
    def reverse_arr(self, arr, start, end):
        if start >= end:
            return 
        arr[start], arr[end] = arr[end], arr[start]
        self.reverse_arr(arr, start + 1, end - 1)

        