class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        tickets.sort()
        adj = collections.defaultdict(list)
        itenary = ["JFK"]

        for src,dest in tickets:
            adj[src].append(dest)
        
        def dfs(src):
            if len(itenary)== len(tickets)+1:
                return True
            if src not in adj:
                return False
            
            temp = adj[src]
            for i,dest in enumerate(temp):
                adj[src].pop(i)
                itenary.append(dest)
                if dfs(dest): return True
                adj[src].insert(i,dest)
                itenary.pop()
            return False
        dfs("JFK")
        return itenary