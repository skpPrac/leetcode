# https://leetcode.com/problems/longest-common-prefix/

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ''

        common_str = strs[0]
        for runner in strs[1:]:
            min_index = min(len(common_str), len(runner))
            i = 0
            while i < min_index:
                if common_str[i] != runner[i]:
                    break
                i += 1
            common_str = common_str[:i]
        return common_str
