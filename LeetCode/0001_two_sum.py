# bad solution, can be improved

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        d = {}

        for i in range(0, len(nums)):
            d[i] = nums[i]

        for i in range(0, len(nums)):

            diff = target - nums[i]
            x = nums[i]
            ans = []

            if diff != nums[i] and diff in nums:

                for key, value in d.items():
                    if x == value:
                        ans.append(key)
                    
                    if diff == value:
                        ans.append(key)
                
                return ans

            elif diff == nums[i]:

                nums.remove(nums[i])
                if diff in nums:
                    for key, value in d.items():
                        if x == value:
                            ans.append(key)
                            continue
                        
                        if diff == value:
                            ans.append(key)
                    
                    return ans
                
