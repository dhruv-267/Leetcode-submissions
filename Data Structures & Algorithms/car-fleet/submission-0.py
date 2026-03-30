class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        hashmap = {}
        for i in range(len(position)):
            hashmap[position[i]] = speed[i]
        hashmap = dict(sorted(hashmap.items(),reverse = True))

        stack = []
        for key in hashmap:
            time = (target - key) / hashmap[key]
            if stack and stack[-1] >= time:
                continue
            else:
                stack.append(time)
        return len(stack)


        