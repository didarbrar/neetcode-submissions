class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars=sorted(zip(position,speed),reverse=True) 
        time=[]
        for pos, spe in cars:
            time.append((target-pos)/spe)
        stack=[]
        for i in range(len(position)):
            if not stack:
                stack.append(time[i])
            elif time[i]>stack[-1]:
                stack.append(time[i])
            else:
                continue
        return len(stack)