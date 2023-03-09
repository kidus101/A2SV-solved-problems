class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # TC:O(N) SC:O(N)
        
        cars = []
        
        for i in range(len(position)):
            cars.append((position[i], speed[i]))
        
        cars.sort(key=lambda x: (x[0], x[1]), reverse=True)
        stack = []
        
        for distance , velocity in cars:
            
            remainin_distance = target - distance
            
            if not stack:
                stack.append(remainin_distance/ velocity) 
                
            elif remainin_distance/ velocity > stack[-1]: 
                stack.append(remainin_distance / velocity)
 
        return len(stack)