class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = {c:set() for w in words for c in w}
        for i in range(len(words)-1):
            w1,w2 = words[i],words[i+1]
            l1,l2 = len(w1),len(w2)
            sml = min(l1,l2)
            if w1[:sml] == w2[:sml] and l1>l2:
                return "" 

            for j in range(sml):
                if w1[j]!=w2[j]:
                    adj[w1[j]].add(w2[j])
                    break
             
        
        visited , cycle = set(), set()
        output = []
        def dfs(c):
            if c in cycle:
                return False
            if c in visited:
                return True
            cycle.add(c)
            
            for nei in adj[c]:
                    if not dfs(nei): return False
            cycle.remove(c)
            visited.add(c)
            output.append(c)
            return True
        
        for c in adj:
            if not dfs(c):
                return ""
        output.reverse()
        return "".join(output)
