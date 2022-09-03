class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        from collections import defaultdict
        
        courseDict = defaultdict(list)
        indegree = {}
        for nextCourse, firstCourse in prerequisites:
            courseDict[firstCourse].append(nextCourse)
            indegree[nextCourse] = indegree.get(nextCourse, 0) + 1
        indegree_zero = [k for k in range(numCourses) if k not in indegree]
        ans = []
        while indegree_zero:
            currCourse = indegree_zero.pop(0)
            ans.append(currCourse)
            for nextCourse in courseDict[currCourse]:
                indegree[nextCourse] -= 1
                if indegree[nextCourse] == 0:
                    indegree_zero.append(nextCourse)
                    del indegree[nextCourse]
            
        return [] if indegree else ans