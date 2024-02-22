class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def bfs(root):
            if not root:
                return []

            que = [root]
            node = []

            while que:
                curr = que.pop()
                if not curr.left and not curr.right:
                    node.append(curr.val)
                if curr.left:
                    que.append(curr.left)
                if curr.right:
                    que.append(curr.right)
            
            return node

        return bfs(root1) == bfs(root2)