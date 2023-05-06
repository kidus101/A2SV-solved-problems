class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
            dic = defaultdict(list)

            for x,y in roads:
                dic[x].append(y)
                dic[y].append(x)
                
            final = []
            maxlen = 0
            
            for i in range(n):
                for j in range(i+1,n):
                    a = dic[i]
                    b = dic[j]
                    final = a+b
                    
                    if( j in dic[i] or i in dic[j]):
                        maxlen=max(maxlen,len(final)-1)
                        
                    else:
                        maxlen=max(maxlen,len(final))
                        
            return maxlen