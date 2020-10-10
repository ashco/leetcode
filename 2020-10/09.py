import collections
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:
    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string.
        """
        if not root: return []

        data = []
        q = collections.deque([root])

        while q:
            node = q.popleft()

            if node:
                data.append(node.val)
                q.append(node.left)
                q.append(node.right)
            else:
                 data.append('#')

        while data[-1] == '#':
            data.pop()

        return ','.join(data)



        # 2,1,3,N,N,4,N,N,5,N,N

#         2
#       1   3
#   N   N   4   N
#         N   5
#           N   N

# '2,1,3,N,N,4,N,N,5,N,N'

    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree.
        """
        if data is '':
            return None

        nodes = data.split(',')
        root = TreeNode(nodes[0])
        i = 1
        queue = deque([root])

        while queue and i <= len(data) - 1:
            node = queue.popleft()
            if data[i] != '#':
                left = TreeNode(data[i])
                node.left = left
                queue.append(left)
            i += 1
            if i > len(data) - 1:
                break
            if data[i] != '#':
                right = TreeNode(data[i])
                node.right = right
                queue.append(right)
            i += 1
        return root


        # for i, val in enumerate(nodes):
        #     nodes[i] = None if val == '#' else TreeNode(int(val))

        # for i, node in enumerate(nodes):

        #     if node != None :
        #         node.left = nodes[(i * 2) + 1]
        #         node.right = nodes[(i * 2) + 2]

        # return nodes[0]
