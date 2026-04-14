class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = { c:set() for word in words for c in word}
        n = len(words)
        for i in range(n-1):
            w1,w2 = words[i],words[i+1]
            l1,l2 = len(w1),len(w2)
            minlen = min(l1,l2)

            if w1[:minlen]==w2[:minlen] and l1>l2:
                return ""
            for j in range(minlen):
                if w1[j]!=w2[j]:
                    adj[w1[j]].add(w2[j])
                    break
        output = []
        cycle , visited = set(), set()
        def dfs(c):
            if c in cycle:
                return False
            if c in visited:
                return True
            cycle.add(c)
            for nei in adj[c]:
                if not dfs(nei):return False
            cycle.remove(c)
            visited.add(c)
            output.append(c)
            return True

        for c in adj:
            if not dfs(c): return ""
        output.reverse()
        return "".join(output)