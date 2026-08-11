class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # for i in range(0, len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if (nums[i] + nums[j]) ==  target:
        #             return [i,j]

        # return []


        seen = {}

        for i in range (0, len(nums)):
            sub =  target - nums[i]

            if sub in seen:
                return [seen[sub] , i]
            seen[nums[i]] = i

        return []










