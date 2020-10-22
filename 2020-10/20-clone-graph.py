# https://leetcode.com/explore/challenge/card/october-leetcoding-challenge/561/week-3-october-15th-october-21st/3501/

# Given a reference of a node in a connected undirected graph.

# Return a deep copy (clone) of the graph.

# Each node in the graph contains a val (int) and a list (List[Node]) of its neighbors.

# class Node {
#     public int val;
#     public List<Node> neighbors;
# }

# Test case format:

# For simplicity sake, each node's value is the same as the node's index (1-indexed). For example, the first node with val = 1, the second node with val = 2, and so on. The graph is represented in the test case using an adjacency list.

# Adjacency list is a collection of unordered lists used to represent a finite graph. Each list describes the set of neighbors of a node in the graph.

# The given node will always be the first node with val = 1. You must return the copy of the given node as a reference to the cloned graph.

import collections

def cloneGraph(node):
    if not node: return []

    clone_d = {}
    q = collections.deque([node])

    clone_d[node] = Node(node.val, [])

    while q:
        curr = q.popleft()

        for n in curr.neighbors:
            if n not in clone_d:
                clone_d[n] = Node(n.val, [])
                q.append(n)
            clone_d[curr].neighbors.append(clone_d[n])
        # clone_d[curr] = Node(curr.val, [clone_d[n] for n in curr.neighbors])

    return clone_d[node]





    # traverse the graph



# print(cloneGraph([[2,4],[1,3],[2,4],[1,3]])) # [[2,4],[1,3],[2,4],[1,3]]
# print(cloneGraph([[]])) # [[]]
# print(cloneGraph([])) # []
# print(cloneGraph([[2],[1]])) # [[2],[1]]