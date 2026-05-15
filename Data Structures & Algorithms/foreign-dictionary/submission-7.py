class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = { c:set() for word in words for c in word}    #use set instead of list and dont use collections.defaultdict(set)
    
        for i in range(len(words)-1):
            w1,w2 = words[i],words[i+1]
            l1,l2 = len(w1),len(w2)
            minlen = min(l1,l2)

            if l2<l1 and w1[:l2]==w2:   #logically incorrect if w1 lexically smaller than w2  
                return ""
            for j in range(minlen):     # add first non equal chars in adjset
                if w1[j]!=w2[j]:
                    adj[w2[j]].add(w1[j])   # {larger : set(smaller)}
                    break

        
        output = []
        cycle , visited = set(), set()
        def dfs(c):
            if c in cycle:
                return False
            if c in visited:
                return True
            cycle.add(c)
            visited.add(c)
            for nei in adj[c]:
                if not dfs(nei):return False
            cycle.remove(c)
            output.append(c)
            return True

        for c in adj:
            if not dfs(c): return ""
        #output.reverse()               #no need to reverse output
        return "".join(output)