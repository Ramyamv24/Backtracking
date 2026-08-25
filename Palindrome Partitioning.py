from typing import List

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def is_palindrome(sub):
            return sub == sub[::-1]

        def backtrack(start, path):
            if start == len(s):
                result.append(path[:])
                return

            for end in range(start + 1, len(s) + 1):
                if is_palindrome(s[start:end]):
                    backtrack(end, path + [s[start:end]])

        result = []
        backtrack(0, [])
        return result


# Main part
if __name__ == "__main__":
    s = input("Enter a string: ")

    solution = Solution()
    result = solution.partition(s)

    print("Palindrome partitions:")
    for partition in result:
        print(partition)