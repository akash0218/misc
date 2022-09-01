from collections import defaultdict
from typing import List


class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        if len(words) == 1:
            return True
        dictu = defaultdict(int)
        for i in range(len(order)):
            dictu[order[i]] = i
        for i in range(len(words)-1):
            ptr1 = 0
            ptr2 = 0
            while ptr1 < len(words[i]) and ptr2 < len(words[i+1]):
                if dictu[words[i][ptr1]] < dictu[words[i+1][ptr2]]:
                    break
                elif dictu[words[i][ptr1]] == dictu[words[i+1][ptr2]]:
                    ptr1 += 1
                    ptr2 += 1
                else:
                    return False
            if ptr1 < len(words[i]) and ptr2 == len(words[i+1]):
                return False
        return True


print(Solution().isAlienSorted(["hello","leetcode"], "hlabcdefgijkmnopqrstuvwxyz"))
