class Solution(object):
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        
        if n < 3:
            return [_n for _n in range(n)]
            
        
        tree = [[] for _ in range(n)]
        
        for x, y in edges:
            tree[x].append(y)
            tree[y].append(x)
            
        q = [index for index, there in enumerate(tree) if len(there) == 1]
        
        while n > 2:
            n -= len(q)
            nextQ = []
            for _q in q:
                there = tree[_q].pop()
                tree[there].remove(_q)
                if len(tree[there]) == 1:
                    nextQ.append(there)
            q = nextQ
        
        return q