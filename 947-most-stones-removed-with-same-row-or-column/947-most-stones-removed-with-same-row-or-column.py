class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        x = defaultdict(list)
        y = defaultdict(list)
        
        for i in stones:
            x[i[0]].append(i[1])
            y[i[1]].append(i[0])
            
        neighbour= 0
        visited = set()
        
        for i in stones:
            if (i[0],i[1]) not in visited:
                
                queue = deque()
                queue.append(i)
                
                while queue:
                    stonex,stoney = queue.popleft()
                    
                    if (stonex,stoney) not in visited:
                        visited.add((stonex,stoney))
                        
                        for j in x[stonex]:
                            queue.append([stonex,j])
                            
                        for j in y[stoney]:
                            queue.append([j,stoney])
                            
                neighbour+=1
                
        return len(stones) - neighbour