class Solution:

    def get_sum_increase(self, nums):
        i = 3
        counter = 0
        while i < len(nums):
            if nums[i] > nums[i - 3]:
                counter += 1
            i += 1
        return counter

with open('/Users/xiaolin/Documents/GitHub/advent_of_code/2021/data/day1.txt') as f:
    input = f.readlines()
nums = []
for depth in input:
    nums.append(int(depth.strip('\n')))

print(Solution().get_sum_increase(nums))
