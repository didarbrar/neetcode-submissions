
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
       stack=[]
       n=len(temperatures)
       result=[0 for _ in range(n)]

       for i in range(n):
        while stack and temperatures[i]>temperatures[stack[-1]]:
            previous_day=stack.pop()
            result[previous_day]=i-previous_day
        stack.append(i)

       return result