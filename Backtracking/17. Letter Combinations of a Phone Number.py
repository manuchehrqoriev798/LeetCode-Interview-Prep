class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        # Define a mapping of digits to letters
        mapping = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }

        def backtrack(index, path):
            # If the path has reached the length of the input digits, add it to the result
            if index == len(digits):
                result.append(''.join(path))
                return

            # Get the letters corresponding to the current digit
            letters = mapping[digits[index]]

            # Explore all possible combinations for the current digit
            for letter in letters:
                # Choose
                path.append(letter)

                # Explore
                backtrack(index + 1, path)

                # Unchoose (backtrack)
                path.pop()

        result = []
        backtrack(0, [])
        return result