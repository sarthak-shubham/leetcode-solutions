class Solution(object):
    def findMissingElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums:
            return []
            
        sorted_nums = sorted(nums)
        start = sorted_nums[0]
        end = sorted_nums[-1]
        
        existing_set = set(sorted_nums)
        missing = []
        
        for num in range(start, end + 1):
            if num not in existing_set:
                missing.append(num)
                
        return missing

