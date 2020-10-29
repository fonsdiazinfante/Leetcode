class Solution(object):
    def confusingNumber(self, N):
        dict = {"0":"0", "1":"1", "6":"9", "8":"8", "9":"6"}
        X = str(N)
        result = []
        for i in X[::-1]:
            if i not in dict:
                return False
            result.append(dict[i])
        return "".join(result)!= X
