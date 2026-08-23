from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def backtrack(start, path):
            result.append(path)

            for i in range(start, len(nums)):
                backtrack(i + 1, path + [nums[i]])

        result = []
        backtrack(0, [])
        return result


# Main part
if __name__ == "__main__":
    nums = [1, 2, 3]

    solution = Solution()
    result = solution.subsets(nums)

    print("Input:", nums)
    print("All subsets:")

    for subset in result:
        print(subset)