class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        new_list = s.split(" ")
        print(new_list)
        
        output = []
        
        for i in range(k):
            output.append(new_list[i])
        
        return " ".join(output)