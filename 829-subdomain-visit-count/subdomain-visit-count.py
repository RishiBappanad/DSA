class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        hashmap = {}
        for i in cpdomains:
            i = i.split(" ")
            print(i)
            count = int(i[0])
            domain = i[1]
            curr = domain
            while len(curr) > 0:
                if curr not in hashmap:
                    hashmap[curr] = 0
                hashmap[curr] += count
                curr = curr.partition('.')[2]
        res = []
        for i in hashmap.keys():
            val = hashmap[i]
            res.append(f"{val} {i}")
        return res