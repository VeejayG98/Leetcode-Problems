class Solution:
    from collections import defaultdict
    
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        courseDict = defaultdict(list)
        for nextCourse, firstCourse in prerequisites:
            courseDict[firstCourse].append(nextCourse)
        
        visited = [False] * numCourses
        loopCheck = [False] * numCourses
        for course in range(numCourses):
            if not visited[course]:
                if self.checkLoop(course, courseDict, visited, loopCheck):
                    return False
        return True
        
    def checkLoop(self, currCourse, courseDict, visited, loopCheck):
        loopCheck[currCourse] = True
        visited[currCourse] = True
        for nextCourse in courseDict[currCourse]:
            if not visited[nextCourse]:
                self.checkLoop(nextCourse, courseDict, visited, loopCheck)
            if loopCheck[nextCourse]:
                return True
        loopCheck[currCourse] = False
        return False