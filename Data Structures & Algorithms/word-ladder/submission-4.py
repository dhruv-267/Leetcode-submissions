class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        wordList.append(beginWord) 
        wordmap = collections.defaultdict(list) #word:[patterns]
        patternmap = collections.defaultdict(list) #pattern : [words]

        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] +"*"+word[i+1:]
                wordmap[word].append(pattern)
                patternmap[pattern].append(word)
        
        visited = set()
        q = collections.deque()
        q.append(beginWord)
        visited.add(beginWord)
        reslen = 1

        while q:
            for i in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return reslen
                for pat in wordmap[word]:
                    for wrd in patternmap[pat]:
                        if wrd == endWord:
                            return reslen+1
                        if wrd not in visited:
                            visited.add(wrd)
                            q.append(wrd)
            reslen+=1 
        return 0