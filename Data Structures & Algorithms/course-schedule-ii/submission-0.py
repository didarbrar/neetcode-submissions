class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        graph={i:[] for i in range(numCourses)}

        for courses,pre in prerequisites:
            graph[courses].append(pre)
        
        visiting=set()
        visited=set()

        result=[]
        
        def dfs(course):
            nonlocal result

            if course in visiting:
                return False
            
            if course in visited:
                return True
            
            visiting.add(course)

            for pre in graph[course]:
                if not dfs(pre):
                    return False
            
            visiting.remove(course)
            result.append(course)
            visited.add(course)

            return True
        
        for course in range(numCourses):
            if not dfs(course):
                return []
        
        return result
        


        
        