class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        
        counter = Counter()
        answer = [set(),set()]
        
        for winner,loser in matches :
            counter[loser] += 1
            
        for winner, loser in matches:
            if counter[winner] == 0:
                answer[0].add(winner)
            if counter[winner] == 1:
                answer[1].add(winner)
            if counter[loser] == 1:
                answer[1].add(loser)
                
        answer[0] = sorted(answer[0])
        answer[1] = sorted(answer[1])
        
        return answer
        
        
                
                
                
                
                
                
            #      for loser in range(len(matches)) :
            # if matches[loser][0] not in loser_dict:
            #     loser_dict[loser] = 1
            # else:
            #     loser_dict[loser][0] += 1
            # if matches[loser][0] not in winner_dict:
            #     winner_dict[winner] = 1
            # else:
            #     winner_dict[winner] += 1
