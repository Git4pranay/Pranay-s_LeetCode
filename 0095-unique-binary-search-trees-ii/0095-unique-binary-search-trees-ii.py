# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        def generate_trees(start, end, memo):
            if start > end:
                return [None]

            if (start, end) in memo:
                return memo[(start, end)]

            all_trees = []
            for root_val in range(start, end + 1):
                left_trees = generate_trees(start, root_val - 1, memo)
                right_trees = generate_trees(root_val + 1, end, memo)

                for left_tree in left_trees:
                    for right_tree in right_trees:
                        root = TreeNode(root_val)
                        root.left = left_tree
                        root.right = right_tree
                        all_trees.append(root)

            memo[(start, end)] = all_trees
            return all_trees

        memo = {}
        return generate_trees(1, n, memo) if n > 0 else []