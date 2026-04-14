class Solution: # could be easily solved with dijksta's algo if not k stops needed
    #for k stops we can update each edge k+1 times using bellmen ford : 
    #(k+1) because k stops between src and dest means k+1 iterations
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        price = [math.inf]*n
        price[src] = 0

        for i in range(k+1):
            tempprice = price.copy()
            for s,d,p in flights:
                if price[s]==math.inf:
                    continue
                if price[s]+p < tempprice[d]:
                    tempprice[d] = price[s]+p
            price = tempprice
        return -1 if price[dst]==math.inf else price[dst]
                
        