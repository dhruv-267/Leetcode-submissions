class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        hashmap = {}
        for i in range(len(position)):
            hashmap[position[i]] = (target-position[i])/speed[i]
        hashmap = dict(sorted(hashmap.items(),reverse = True))

        stack = []
        for key in hashmap:
            if stack and stack[-1] >= hashmap[key]:
                continue
            else:
                stack.append(hashmap[key])
        return len(stack)


        