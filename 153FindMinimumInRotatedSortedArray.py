class Solution:
    def findMin(self, nums) -> int:
        l = 0
        r = len(nums) - 1

        while l < r:
            m = l + ((r - l) // 2)

            if nums[l] < nums[r]:
                r = m
            elif nums[l] > nums[r]:
                l = m


        return nums[l]
        