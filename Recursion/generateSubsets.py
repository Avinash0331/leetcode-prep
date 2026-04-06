def generateSubsets(nums):
    def backtrack(idx, path):
        # Base case: reached end of array, print current subset
        if idx == len(nums):
            print(path)
            return

        # Decision 1: Skip current element
        backtrack(idx + 1, path)

        # Decision 2: Include current element
        path.append(nums[idx])
        backtrack(idx + 1, path)

        # Undo choice (backtrack)
        path.pop()

    backtrack(0, [])


# Example: generates all subsets of [1,2,3]
generateSubsets([1, 2, 3])

# Dry run for [1,2] - Decision Tree:
# backtrack(0, []):
#   - Decision 1: Skip 1 → backtrack(1, []):
#     - Decision 1: Skip 2 → backtrack(2, []) → print []
#     - Decision 2: Include 2 → backtrack(2, [2]) → print [2]
#   - Decision 2: Include 1 → backtrack(1, [1]):
#     - Decision 1: Skip 2 → backtrack(2, [1]) → print [1]
#     - Decision 2: Include 2 → backtrack(2, [1,2]) → print [1,2]
# Subsets: [], [2], [1], [1,2]
generateSubsets([1, 2])