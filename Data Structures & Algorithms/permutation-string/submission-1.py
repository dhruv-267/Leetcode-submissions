class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        maps1 , maps2 = {}, {}
        match = 0
        l = 0
        for i in range(len(s1)):
            maps1[s1[i]] = 1 + maps1.get(s1[i],0)
            maps2[s2[i]] = 1 + maps2.get(s2[i],0)
        for key in maps1:
            if key in maps2 and maps1[key]==maps2[key]:
                match +=1
        i = 0
        for j in range(len(s1),len(s2)):
            if match == len(maps1):
                return True
            maps2[s2[j]] = 1 + maps2.get(s2[j],0) 
            if s2[j] in maps1:
                if maps1[s2[j]] == maps2[s2[j]]:
                    match+=1
                elif maps1[s2[j]] +1 == maps2[s2[j]]:
                    match -= 1
            maps2[s2[i]] -= 1
            if s2[i] in maps1:
                if maps1[s2[i]] == maps2[s2[i]]:
                    match+=1
                elif maps1[s2[i]] - 1 == maps2[s2[i]]:
                    match -= 1
            i+=1
        return match == len(maps1)