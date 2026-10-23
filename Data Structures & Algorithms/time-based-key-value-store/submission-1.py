class TimeMap:

    def __init__(self):
        self.my_dict={}
        self.time={}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
         if key not in self.my_dict:

            self.my_dict[key] = []
            self.time[key] = []

         self.my_dict[key].append(value)
         self.time[key].append(timestamp)

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.time:
            return ""
        times=self.time[key]
        target=timestamp
        left=0
        right=len(times)-1
        while left<=right:
            mid=(left+right)//2
            if times[mid]==target:
                return self.my_dict[key][mid]
            elif times[mid]<target:
                left=mid+1
            else:
                right=mid-1
        if right < 0:
            return ""
        return self.my_dict[key][right]
