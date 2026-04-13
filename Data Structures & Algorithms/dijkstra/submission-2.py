class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:
        #greedy algo 

        adj = { i:[] for i in range(n)} #adjucancy matrix for each vertice
        for n1,n2,w in edges:
            adj[n1].append((w,n2))      # add (weight,node) in adj matrix.. where node is neighbour and weight is weight of edge.
        
        shortest = {}                   #result Dict
        minheap = [(0,src)]             # minHeap to select closest node greedily. Add(0,scr) to heap for source node and its distance to itself is 0.
        while minheap:
            w1,n1 = heapq.heappop(minheap)      #pop edges with lowest weight greedily
            if n1 in shortest:                  # if node already in shortest then it already has its min dist as we are popping ele greedily
                continue                       
            shortest[n1] = w1                   # add new node in shortest and min dist value if not already in dict

            for w2,n2 in adj[n1]:               # push all neighbours to minheap if neighbour not in shortest 
                if n2 in shortest:              # if neighbour already in shortest skip as it has already found min dist
                    continue
                heapq.heappush(minheap,(w1+w2,n2))  # w1+w2 because we want to add dist from scr.. not from parent/neighbour node
        
        for i in range(n):
            if i not in shortest:               #if any node not in shortest, it means it is unreachable from src
                shortest[i] = -1                # assign -1
        return shortest
