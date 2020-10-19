class Solution():
    def serialize(self, root: 'Node') -> str:
        """Encodes a tree to a single string.

        :type root: Node
        :rtype: str
        """

        q = collections.deque([root, '|'])
        res = []

        while q:
            node = q.leftpop()

            # end of row
            if node == '|':
                res.append(None)
                q.append('|')
            # no children
            elif node == '_':
                res.append(None)
            # new node
            else:
                res.append(node.val)
                # build queue
                q += node.children if node.children else '_'

        return str(res)

foo = ','.join(map(lambda x : str(x), [1, 3, None, 5]))
print(foo.split(','))