class Solution(object):
    def longestWord(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
       
        words.sort()
        wordDict = {}
        res = ""
        
        for word in words:
            if len(word) == 1 or word[:-1] in wordDict:
                res = word if len(word) > len(res) else res
                wordDict[word] = True
        
        return res
