class Solution:
    def sortPeople(self, names: List[str], array: List[int]) -> List[str]:
        
        for i in range(len(array)):
            for j in range(i + 1 , len(array)):
                if array[i] < array[j]:
                    
                    temp = array[i]
                    array[i] = array[j]
                    array[j] = temp
                    
                    cur = names[i]
                    names[i] = names[j]
                    names[j] = cur
                    
        return names

#         list_ = list()
#         for i in range(len(names)):
#             list_.append([names[i],heights[i]])
#         print(list_)
        
#         for name , height in list_:
#             if height[i] > height