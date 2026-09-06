class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        candidates = sorted(candidates)

        res = []

        def combSum(index, subset, total):

            if total == target:
                res.append(subset.copy())
                return

            if index >= len(candidates) or total > target:
                return

            subset.append(candidates[index])
            combSum(index+1, subset, total + candidates[index])

            subset.pop()

            while (index+1)<len(candidates) and candidates[index+1] == candidates[index]:
                index += 1

            combSum(index+1, subset, total)

        combSum(0, [], 0)

        return res