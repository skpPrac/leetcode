# https://leetcode.com/problems/zigzag-conversion/

class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1 or numRows >= len(s):
            return s
        output = []
        for i in range(0, numRows):
            runner = i
            while runner < len(s):
                output.append(s[runner])
                if i > 0 and i < numRows-1:
                    middle_index = runner + ((numRows - 1 - i) * 2)
                    if middle_index < len(s):
                        output.append(s[middle_index])
                runner = runner + (numRows + numRows - 2)
        return ''.join(output)
