class TimeMap:

    def __init__(self):

        self.time_dict = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:

        if key in self.time_dict:
            self.time_dict[key].append((value,timestamp))
        else:
            self.time_dict[key] = [(value,timestamp)]

        

    def get(self, key: str, timestamp: int) -> str:
        
        if key in self.time_dict:
            arr = self.time_dict[key]
        else:
            return ""

        low = 0
        high = len(arr)-1

        while low <= high:

            mid = (high+low)//2

            if arr[mid][1]<timestamp:
                low = mid + 1
            elif arr[mid][1]>timestamp:
                high = mid - 1
            else:
                return arr[mid][0]

        if arr[mid][1]>timestamp:
            mid -= 1
        
        if arr[mid][1]>timestamp:
            return ""
            
        return arr[mid][0]


        
