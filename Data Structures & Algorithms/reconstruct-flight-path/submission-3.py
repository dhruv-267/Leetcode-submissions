class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        tickets.sort()
        adj = collections.defaultdict(list)
        for src,dest in tickets:
            adj[src].append(dest)
        res = ["JFK"]
        def dfs(src):
            if len(res)== len(tickets)+1:
                return True
            if src not in adj:
                return False

            temp = adj[src]
            for index,dest in enumerate(temp):
                res.append(dest)
                adj[src].pop(index)     # pop specifically at ith place in adj list as it may have multiple enteries of dest
                if dfs(dest): return True
                res.pop()
                adj[src].insert(index,dest)
            return False

        
        dfs("JFK")
        return res