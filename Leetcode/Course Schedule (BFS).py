class Solution:
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        pre = [[] for _ in range(numCourses)]
        to = [0 for _ in range(numCourses)]
        isVisited = [0 for _ in range(numCourses)]
               
        
        for A, B in prerequisites: # B -> A
            pre[A].append(B)
            to[B] += 1
            
            
        q = [i for i in range(numCourses) if to[i] == 0]
        count = 0
        
        while q:
            cur = q.pop(0)
            count += 1
            for i in pre[cur]:
                to[i] -= 1
                if to[i] == 0:
                    q.append(i)
            
        if count == numCourses:
            return True
        else:
            return False