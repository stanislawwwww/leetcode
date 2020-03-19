from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        element_to_number = dict([(x[1], x[0]) for x in enumerate(nums)])
        for i, num in enumerate(nums):
            if (target - num) in element_to_number and i != element_to_number[target - num]:
                return i, element_to_number[target - num]


if __name__ == "__main__":
    print(Solution().twoSum([3,2,4], 6))
    print(Solution().twoSum([2, 7, 11, 15], 9))
    
