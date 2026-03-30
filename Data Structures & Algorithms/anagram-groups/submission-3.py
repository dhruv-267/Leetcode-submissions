class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}
        for str in strs:
            chars = Counter(str)
            if tuple(sorted(chars.items())) in hashmap:
                hashmap[tuple(sorted(chars.items()))].append(str)
            else:
                hashmap[tuple(sorted(chars.items()))] = [str]
        return list(hashmap.values())
        