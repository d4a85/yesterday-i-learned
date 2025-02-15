class Solution:
    def fib(self, n: int) -> int:
        nums = [0] * (n + 3)
        nums[1] = 1
        for i in range(2, n + 1):
            nums[i] = nums[i - 2] + nums[i - 1]

        return nums[n]
