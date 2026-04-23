class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2)<len(s1):
            return False
        s1map = collections.defaultdict(int)
        s2map = collections.defaultdict(int)

        for i in range(len(s1)):
            s1map[s1[i]]+=1
            s2map[s2[i]]+=1
        
        match = 0
        for char in s1map:
            if char in s2map and s1map[char] == s2map[char]:
                match+=1
        i = 0
        for j in range(len(s1),len(s2)):
            if match == len(s1map):
                return True
            
            s2map[s2[j]]+=1
            if s2[j] in s1map:
                if s2map[s2[j]] == s1map[s2[j]]:
                    match+=1
                elif s2map[s2[j]] == s1map[s2[j]]+1:
                    match -=1
            
            s2map[s2[i]]-=1
            if s2[i] in s1map:
                if s2map[s2[i]] == s1map[s2[i]]:
                    match+=1
                elif s2map[s2[i]] + 1 == s1map[s2[i]]:
                    match -=1
            i+=1
        return match == len(s1map)