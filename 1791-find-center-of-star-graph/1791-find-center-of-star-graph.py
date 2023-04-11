class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        if len(edges) == 1:
            return edges[0][0]
        elif edges[0][0] == edges[1][0] or edges[0][0] == edges[1][1]:
            return edges[0][0]
        else:
            return edges[0][1]

# class Solution:
#     def findCenter(self, edges: List[List[int]]) -> int:
#         return list(set(edges[0]) .intersection(edges[1] ))[0]
       
            
        