# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        return self.find_it(1, n)
        
    def find_it(self, first, last):
        if isBadVersion(first):
            return first
        mid = (first + last)/2
        if isBadVersion(mid):
            return self.find_it(first, mid)
        else:
            return self.find_it(mid+1, last)
