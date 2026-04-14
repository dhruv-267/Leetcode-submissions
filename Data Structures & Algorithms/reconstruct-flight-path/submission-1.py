class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        tickets.sort()
        adj = collections.defaultdict(list)

        for src,dest in tickets:
            adj[src].append(dest)
        
        res = ["JFK"]

        def dfs(src):
            if len(res) == len(tickets)+1:
                return True
            if src not in adj:
                return False
            
            temp = adj[src]
            for i,dest in enumerate(temp):
                res.append(dest)
                adj[src].pop(i)
                if dfs(dest) : return True
                res.pop()
                adj[src].insert(i,dest)
            return False

        
        dfs("JFK")
        return res