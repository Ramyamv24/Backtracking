from typing import List

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        def backtrack(start, subset):
            result.append(subset[:])

            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i - 1]:
                    continue

                subset.append(nums[i])
                backtrack(i + 1, subset)
                subset.pop()

        nums.sort()
        result = []
        backtrack(0, [])
        return result


# Main part
if __name__ == "__main__":
    nums = [1, 2, 2]

    solution = Solution()
    result = solution.subsetsWithDup(nums)

    print("Input:", nums)
    print("Subsets with duplicates removed:")

    for subset in result:
        print(subset)