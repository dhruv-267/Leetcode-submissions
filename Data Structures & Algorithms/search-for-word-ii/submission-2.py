class TrieNode:
    def __init__(self):
        self.children = {}
        self.isword = False
    
    def addWord(self,word):
        cur = self

        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.isword = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        
        root = TrieNode()
        for word in words:
            root.addWord(word)
        row = len(board)
        col = len(board[0])
        visited = set()
        res = set()

        def dfs(r,c,node,word):
            if r<0 or c<0 or r>row-1 or c>col-1 or (r,c) in visited or board[r][c] not in node.children:
                return
            
            visited.add((r,c))
            node = node.children[board[r][c]]
            word+=board[r][c]
            if node.isword:
                res.add(word)
            
            dfs(r+1,c,node,word)
            dfs(r,c+1,node,word)
            dfs(r-1,c,node,word)
            dfs(r,c-1,node,word)

            visited.remove((r,c))
        for i in range(row):
            for j in range(col):
                dfs(i,j,root,"")
        return list(res)

        