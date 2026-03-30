class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        result = defaultdict(list)
        for s in strs:
            alphabets = [0]*26
            for i in s:
                alphabets[ord(i)-97] +=1
       
            result[tuple(alphabets)].append(s)
            
        return list(result.values())



