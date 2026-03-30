class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}  #{anagram : [str]}
        
        for str in strs:
            charArr = [0]*26
            for c in str:
                index = ord(c)-ord('a')
                charArr[index]+=1
            if tuple(charArr) in hashmap:
                hashmap[tuple(charArr)].append(str)
            else:
                hashmap[tuple(charArr)] = [str]
        
        return list(hashmap.values())