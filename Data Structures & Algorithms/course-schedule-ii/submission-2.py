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
            if crs in finishable:
                return True
            
            cycle.add(crs)
            for pre in premap[crs]:
                if not dfs(pre): return False
            cycle.remove(crs)
            finishable.add(crs)
            output.append(crs)
            premap[crs]=[]
            return True
        
        for i in range(numCourses):
            if not dfs(i): return []
        return output         

        

        