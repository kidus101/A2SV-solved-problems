class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        
        dict_ = { 5:0 , 10:0 , 20:0 }
        
        for bill in bills:
            if bill == 5:
                dict_[5] += 1
                
            if bill == 10:
                if dict_[5] >= 1:
                    dict_[5] -= 1
                    dict_[10] += 1
                else:
                    return False
                
            if bill == 20:
                if dict_[10] >= 1 and dict_[5] >= 1:
                    dict_[5] -= 1
                    dict_[10] -= 1
                    
                elif dict_[5] >= 3:
                    dict_[5] -= 3
                    
                else:
                    return False
            
        return True
                
            
                
       
        