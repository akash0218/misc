from collections import deque


class Solution:
    def alienOrder(self, words: list[str]) -> any:
        alphabets = 'abcdefghijklmnopqrstuvwxyz'
        dictu = {}
        indegrees = [0]*26
        for i in words:
            for j in i:
                if j not in dictu:
                    dictu[j] = set()
        for i in range(len(words)-1):
            ptr1 = 0
            ptr2 = 0
            while ptr1 < len(words[i]) and ptr2 < len(words[i+1]):
                if words[i][ptr1] == words[i+1][ptr2]:
                    ptr1 += 1
                    ptr2 += 1
                else:
                    if words[i+1][ptr2] not in dictu[words[i][ptr1]]:
                        dictu[words[i][ptr1]].add(words[i+1][ptr2])
                        indegrees[ord(words[i+1][ptr2])-ord('a')] += 1
                    break
            # ['abcd', 'abc'] --> here ptr2 finishes before ptr1 but it is not in lexicographical order.
            # so we reset the dictionary.
            if ptr2 == len(words[i+1]) and len(dictu) > 1 and words[i][0] == words[i+1][0]:
                dictu = {}
                break
        result = []
        queue = deque()
        for i in range(len(indegrees)):
            if indegrees[i] == 0 and alphabets[i] in dictu:
                queue.append(alphabets[i])
        if len(queue) == 0:
            return ''
        while queue:
            pop = queue.popleft()
            result.append(pop)
            for i in dictu[pop]:
                indegrees[ord(i)-ord('a')] -= 1
                if indegrees[ord(i)-ord('a')] == 0:
                    queue.append(i)
        # result should have atleast the number of characters as in dictionary
        # else we were stuck somewhere and there exists a cycle.
        if len(result) != len(dictu):
            return ''
        return ''.join(result)


print(Solution().alienOrder(['z', 'x', 'a', 'zb', 'zx']))
