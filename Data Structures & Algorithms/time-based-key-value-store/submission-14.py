class TimeMap:

    def __init__(self):

        self.time_dict = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:

        if key in self.time_dict:
            self.time_dict[key].append((value,timestamp))
        else:
            self.time_dict[key] = [(value,timestamp)]

        

    def get(self, key: str, timestamp: int) -> str:

        if key not in self.time_dict:
            return ""

        arr = self.time_dict[key]

        low, high = 0, len(arr)-1
        res = ""

        while low <= high:

            mid = (high + low)//2

            if arr[mid][1] <= timestamp:
                low = mid + 1

                res = arr[mid][0]

            else:

                high = mid - 1

        return res

        
