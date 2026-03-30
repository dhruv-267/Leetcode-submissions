class TimeMap:

    def __init__(self):
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.store:
            self.store[key].append([value,timestamp])
        else:
            self.store[key] = [[value,timestamp]]       

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""
        else:
            arr = self.store[key]
            low , high = 0 , len(arr)-1
            res = ""
            
            while low <=high :
                mid = (low+high)//2
                if arr[mid][1]==timestamp:
                    res =  arr[mid][0]
                    return res
                elif arr[mid][1] > timestamp:
                    high = mid - 1
                else:
                    res = arr[mid][0]
                    low = mid + 1
        return res

        
