class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = defaultdict(list)
        for src, dst in sorted(tickets)[::-1]:
            adj[src].append(dst)

        
        res = []
        source = ["JFK"]
        while source:
            curr = source[-1]
            if not adj[curr]:
                res.append(source.pop())
            else:
                source.append(adj[curr].pop())

        return res[::-1]