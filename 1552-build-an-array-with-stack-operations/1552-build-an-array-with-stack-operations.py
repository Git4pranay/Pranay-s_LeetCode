class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        res = []  # Initialize an empty result list
        cur = 1  # Initialize the current number to 1

        for num in target:
            while cur < num:
                # Push elements from 1 to num - 1 into the result list
                res.append("Push")
                res.append("Pop")
                cur += 1

            # Push the current number into the result list
            # Current number should be a target number right now
            res.append("Push")
            cur += 1

        return res    