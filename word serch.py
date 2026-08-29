from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])

        def dfs(r, c, i):
            if (
                r < 0 or r >= m or
                c < 0 or c >= n or
                board[r][c] != word[i]
            ):
                return False

            if i == len(word) - 1:
                return True

            tmp = board[r][c]
            board[r][c] = '#'

            found = (
                dfs(r - 1, c, i + 1) or
                dfs(r + 1, c, i + 1) or
                dfs(r, c - 1, i + 1) or
                dfs(r, c + 1, i + 1)
            )

            board[r][c] = tmp

            return found

        for i in range(m):
            for j in range(n):
                if dfs(i, j, 0):
                    return True

        return False


# Main Part
if __name__ == "__main__":
    board = [
        ['A', 'B', 'C', 'E'],
        ['S', 'F', 'C', 'S'],
        ['A', 'D', 'E', 'E']
    ]

    word = "ABCCED"

    solution = Solution()

    result = solution.exist(board, word)

    print(result)