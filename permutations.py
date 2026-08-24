from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def perms(i):
            if i == len(nums):
                res.append(nums[:])
                return

            for j in range(i, len(nums)):
                nums[i], nums[j] = nums[j], nums[i]
                perms(i + 1)
                nums[i], nums[j] = nums[j], nums[i]

        perms(0)
        return res


# Main part
if __name__ == "__main__":
    nums = [1, 2, 3]

    solution = Solution()
    result = solution.permute(nums)

    print("All permutations:")
    for permutation in result:
        print(permutation)