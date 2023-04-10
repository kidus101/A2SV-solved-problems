class Solution:
	def largestMerge(self, word1: str, word2: str) -> str:
		list1 = list(word1)
		list2 = list(word2)

		output = []
        # print(list1)
        
		while list1 and list2:
            
			if list1 > list2:
				output.append(list1[0])
				list1.pop(0)
                
			else:
				output.append(list2[0])
				list2.pop(0)

		return "".join( output + list1 + list2 )