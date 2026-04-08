class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        hashmap = {}
        stack = []
        for i in range(len(position)):
            hashmap[position[i]] = (target-position[i])/speed[i]
        
        hashmap = dict(sorted(hashmap.items(),reverse = True))

        for key in hashmap:
            if stack and hashmap[key]<=stack[-1]:
                continue
            else: 
                stack.append(hashmap[key])
        return len(stack)

        