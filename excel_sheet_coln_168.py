# https://leetcode.com/problems/excel-sheet-column-title/
class Solution:
    # @param {integer} n
    # @return {string}
    def convertToTitle(self, n):
        return self.excel(n, '')
    
    def excel(self, n, out):
        if n == 0:
            return out
        elif n < 26:
            return '{}{}'.format(chr(n+64), out)
        else:
            rem = n % 26
            n = n/26
            if rem == 0:
                n = n - 1
                rem = 26
            return self.excel(n, '{}{}'.format(chr(rem+64), out))
