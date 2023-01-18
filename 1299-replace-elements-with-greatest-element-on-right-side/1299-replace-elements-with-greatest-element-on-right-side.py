class Solution:
    def replaceElements(self, array: List[int]) -> List[int]:
        max_ = -1
        len_array = len(array)
        
        for i in range(len(array)-1 , -1 , -1):
            value = array[i]
            array[i] = max_
            max_ = max(value,max_)
        return array

                