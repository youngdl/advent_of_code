class Solution:

    def get_increases(self, input):
        counter = 0
        i = 1
        while i < len(input):
            if input[i] > input[i - 1]:
                counter += 1
            i += 1
        return counter

with open('/Users/xiaolin/Documents/GitHub/advent_of_code/2021/data/day1.txt') as f:
    input = f.readlines()
nums = []
for depth in input:
    nums.append(int(depth.strip('\n')))
print(Solution().get_increases(nums))
