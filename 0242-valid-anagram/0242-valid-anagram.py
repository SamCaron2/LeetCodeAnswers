class Solution(object):
    def isAnagram(self, s, t):
        str = []
        tsr = []

        str.extend(s)
        tsr.extend(t)
        str.sort()
        tsr.sort()

        if tsr == str:
            return True
        else:
            return False
        