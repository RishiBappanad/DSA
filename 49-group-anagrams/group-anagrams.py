class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        wordmap = {} #key : str(hashmap) -> #value : [words]
        def serialize(hashmap):
            string = ""
            for i in sorted(hashmap.keys()):
                string += f"{i}:{hashmap[i]}"
            return string
        for i in strs:
            hashmap = {}
            for j in i:
                if j not in hashmap:
                    hashmap[j] = 0
                hashmap[j] += 1
            hashmap = serialize(hashmap)
            if hashmap not in wordmap:
                wordmap[hashmap] = []
            wordmap[hashmap].append(i)
        for i in wordmap.keys():
            res.append(wordmap[i])
        return res