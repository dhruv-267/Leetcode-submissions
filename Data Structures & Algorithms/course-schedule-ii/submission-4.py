class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        premap = { i:[] for i in range(numCourses)}
        for crs,pre in prerequisites:
            premap[crs].append(pre)
        finishable,cycle = set(),set()
        output = []

        def dfs(crs):
            if crs in cycle:
                return False

            #if premap[crs]==[]:        if we use 'premap[crs]==[]' condition instead of 'crs in finishable': 
            if crs in finishable:       #then we skip all the courses with zero prerequisite to add in our result.
                return True             #with 'crs in finishable' we skip course only if it is already added in result.
            
            cycle.add(crs)
            for pre in premap[crs]:
                if not dfs(pre): return False
            cycle.remove(crs)
            finishable.add(crs)
            output.append(crs)
            return True
        
        for i in range(numCourses):
            if not dfs(i): return []
        return output         

        

        