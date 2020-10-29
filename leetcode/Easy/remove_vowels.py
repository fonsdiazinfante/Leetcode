class Solution(object):
    def removeVowels(self, S):
        a = {"a","e","i","o","u"}
        sb = ""
        for i in S:
            if i not in a:
                sb = sb + i
        return sb
        
