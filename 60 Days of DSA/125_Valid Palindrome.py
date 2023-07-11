class Solution:
    def isPalindrome(self, s: str) -> bool:
        punctuations = '''!()-[]{};:'`"\,<>./?@#$%^&*_~'''
        result = "".join([c.lower() for c in s if c not in punctuations])
        result = result.replace(" ", "")
        return self.checkPalindrome(result, 0, len(result) - 1)

    def checkPalindrome(self, s, l, r):
        return s == s[::-1]
    

    """Input: s = "A man, a plan, a canal: Panama"
        Output: true
        Explanation: "amanaplanacanalpanama" is a palindrome."""