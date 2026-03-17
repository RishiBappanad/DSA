from datetime import datetime, timedelta
from collections import deque
class Solution:
    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
        hashmap = {} #keep rolling list of last 3 scans
        res = []
        hour = timedelta(hours=1)
        for i in range(len(keyName)):
            name = keyName[i]
            time = keyTime[i]
            if name not in hashmap:
                hashmap[name] = [time]
            else:
                hashmap[name].append(time)
        for i in hashmap.keys():
            hashmap[i] = sorted(hashmap[i])
            for j in range(len(hashmap[i]) - 2):
                times = hashmap[i]
                first = datetime.strptime(times[j], "%H:%M")
                recent = datetime.strptime(times[j + 2], "%H:%M")
                if recent - first <= hour:
                    res.append(i)
                    break
        return sorted(res)
