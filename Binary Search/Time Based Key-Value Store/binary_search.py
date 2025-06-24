from collections import defaultdict

class TimeMap:

    def __init__(self):
        self.hash_map = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.hash_map[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        list_ts = self.hash_map[key]
        start, end = 0, len(list_ts)-1
        while start<=end:
            mid = start+((end-start)//2)
            if list_ts[mid][0]>timestamp:
                end = mid-1
            else:
                start = mid+1
        if end<0:
            return ""
        return list_ts[end][1]
