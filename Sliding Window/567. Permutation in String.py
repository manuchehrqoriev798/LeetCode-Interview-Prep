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