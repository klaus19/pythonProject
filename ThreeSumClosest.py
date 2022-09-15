from typing import List


class ThreeSumClosest:
    def findThreeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        res = sum(nums[:3])
        for i in range(len(nums)):
            l,r=i+1,len(nums)-1
            while l<r:
                s = sum((nums[i],nums[1],nums[r]))
                if abs(s - target) < abs(res - target):
                    res = s
                if s < target:
                    l += 1
                elif s > target:
                    r -= 1
                else:  # break early
                    return res
                return res
