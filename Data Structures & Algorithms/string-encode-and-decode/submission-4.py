class Solution:

    def encode(self, strs: List[str]) -> str:
        encodedstr = ''
        for s in strs:
            encodedstr += str(len(s)) + "#" + s
        return encodedstr

    def decode(self, s: str) -> List[str]:
        i = 0
        res = []
        print(s)
        while i < len(s):
            j = i
            while s[j] != '#':
                j+=1
            lenS = int(s[i:j])
            res.append(s[j+1:j+1+lenS])
            i = j+lenS+1
        return res