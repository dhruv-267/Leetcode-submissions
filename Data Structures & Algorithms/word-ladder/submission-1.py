class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        wordList.append(beginWord)
        adj = collections.defaultdict(list)
        patternmap = collections.defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i]+"*"+word[i+1:]
                adj[pattern].append(word)
                patternmap[word].append(pattern)
        
        visited = set()
        q = collections.deque()
        q.append(beginWord)
        visited.add(beginWord)
        res = 1
        while q:
            for i in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return res
                for pat in patternmap[word]:
                    for wrd in adj[pat]:
                        if wrd not in visited:
                            q.append(wrd)
                            visited.add(wrd)
            res+=1
        return 0

