class Solution(object):
    def containsDuplicate(self, nums):
        str1 = set()
        

        for num in nums:
            if num in str1:
                return True
            else:
                str1.add(num)
            
