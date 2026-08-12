class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        temp={}

        for i in range (0,len(nums)):
            if nums[i] in temp:
                temp[nums[i]] +=1
            else:
                temp[nums[i]] = 1

        sorted_nums = sorted(temp, key=temp.get, reverse=True)

        return sorted_nums[:k]
        