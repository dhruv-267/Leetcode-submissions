class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for s in strs:
            encoded += str(len(s)) + "#" +s
        return encoded    

    def decode(self, s: str) -> List[str]:
        decoded = []
        i , j = 0,0
        while j < len(s):
            if s[j]=='#':
                length = int(s[i:j])
                decoded.append(s[j+1:j+1+length])
                i = j+1+length
                j = j+1+length
            else:
                j+=1
        return decoded
