class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        count = 0

        for letter in s[:k]:
            if letter in vowels:
                count += 1

        res = count

        for i in range(k, len(s)):
            if s[i - k] in vowels:
                count -= 1
            if s[i] in vowels:
                count += 1

            if count > res:
                res = count

        return res
