from collections import defaultdict
class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
       
        d = defaultdict(int)
        ans = []
        for item in cpdomains:
            count, domain = item.split(" ")
            *subdomains, = domain.split(".")
            for i in range(len(subdomains)):
                d[".".join(subdomains)] += int(count)
                subdomains.pop(0)
        for key,val in d.items():
            temp = str(val) + " " + key
            ans.append(temp)
        return ans
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         dic = collections.defaultdict(int)
        
#         for cpdomain in cpdomains:
#             count , domain = cpdomain.split(' ')
#             count = int(count)
            
#             currentDomain = ""
#             for substring in domain.split('.')[::-1]:
#                 if currentDomain == "":
#                     currentDomain = substring
#                 else:
#                     currentDomain = substring + "." + currentDomain
#                 dic[currentDomain] +=  count
            
#             results = []
            
#             for key in dic.keys():
#                 results.append(str(dic[key]) + " " + key)
            
#             return results
          
#             # TC:O(N^2) & SC:O(N)
        