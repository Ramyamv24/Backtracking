from typing import List

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(i):
            if i == len(nums):
                res.append(nums[:])
                return

            seen = set()

            for j in range(i, len(nums)):
                if nums[j] in seen:
                    continue
                seen.add(nums[j])

                nums[i], nums[j] = nums[j], nums[i]
                backtrack(i + 1)
                nums[i], nums[j] = nums[j], nums[i]  # backtrack

        backtrack(0)
        return res


# Main part
if __name__ == "__main__":
    nums = [1, 1, 2]

    solution = Solution()
    result = solution.permuteUnique(nums)

    print("Unique permutations:")
    for permutation in result:
        print(permutation)