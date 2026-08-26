class Solution(object):
    def letterCasePermutation(self, S):
        res = []

        def backtrack(sub="", i=0):
            if len(sub) == len(S):
                res.append(sub)
            else:
                if S[i].isalpha():
                    backtrack(sub + S[i].swapcase(), i + 1)
                backtrack(sub + S[i], i + 1)

        backtrack()
        return res


# Main part
S = input("Enter a string: ")

obj = Solution()
result = obj.letterCasePermutation(S)

print("Letter Case Permutations:")
for x in result:
    print(x)