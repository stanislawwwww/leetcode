#from collections import OrderedDict

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        current_sequnce = set()
        current_sequnce.add(s[0])
        current_max_length = 1
        current_start_p = 0
        current_end_p = 0
        for i in range(1, len(s)):
            if s[i] not in current_sequnce:
                    current_sequnce.add(s[i])
                    current_end_p = i
                    current_max_length = max(current_end_p - current_start_p + 1, current_max_length)
                    # print('{} not in current_seq {} adding, max = {}'.format(s[i], current_sequnce, current_max_length))
                    continue
            while s[i] in current_sequnce:
                current_sequnce.remove(s[current_start_p])
                # print('removing from sequence {} {}'.format(current_sequnce, s[current_start_p]))
                current_start_p += 1
            current_sequnce.add(s[i])
            current_end_p = i
        return current_max_length

        
if __name__ == "__main__":
    solver = Solution()
    print(solver.lengthOfLongestSubstring("abcabcbb"))
    assert solver.lengthOfLongestSubstring("abcabcbb") == 3
    print(solver.lengthOfLongestSubstring("bbbbb"))
    assert solver.lengthOfLongestSubstring("bbbbb") == 1
    print(solver.lengthOfLongestSubstring("pwwkew"))
    assert solver.lengthOfLongestSubstring("pwwkew") == 3
    print(solver.lengthOfLongestSubstring("qwerty"))
    assert solver.lengthOfLongestSubstring("qwerty") == 6
    print(solver.lengthOfLongestSubstring(""))