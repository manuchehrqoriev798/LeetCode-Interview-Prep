class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1Count, s2Count = [0] * 26, [0] * 26

        for i in range(len(s1)):
            s1Count[ord(s1[i]) - ord('a')] += 1
            s2Count[ord(s2[i]) - ord('a')] += 1

        for i in range(len(s1), len(s2)):
            if s1Count == s2Count:
                return True

            s2Count[ord(s2[i]) - ord('a')] += 1
            s2Count[ord(s2[i - len(s1)]) - ord('a')] -= 1

        return s1Count == s2Count



class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        if len(s1) > len(s2):
            return False

        s1_count = Counter(s1)
        window_count = Counter(s2[:len(s1)])

        for i in range(len(s2) - len(s1)):
            if s1_count == window_count:
                return True
            window_count[s2[i]] -= 1
            if window_count[s2[i]] == 0:
                del window_count[s2[i]]
            window_count[s2[i + len(s1)]] += 1
            
        return s1_count == window_count




0n^2
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l, r = 0, 0
        q = deque([])

        for char in s1:
            q.append(char)
        
        while r < len(s2):
            if s2[r] in q:
                q.remove(s2[r])
                r += 1
            else:
                q.append(s2[l])
                l += 1

            if len(q) == 0:
                return True
        
        return len(q) == 0






0n^2
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l = 0
        r = 0
        arrayS1 = []
        for letter in s1:
            arrayS1.append(letter)

        while r < len(s2):
            if s2[r] in arrayS1:
                arrayS1.remove(s2[r])
                r += 1
            else:
                arrayS1.append(s2[l])
                l += 1

            if not arrayS1:
                return True

        return False