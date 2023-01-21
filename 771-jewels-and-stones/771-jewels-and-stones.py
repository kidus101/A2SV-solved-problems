class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        dic =defaultdict(int)
        # counted_stones = Counter(stones)
        count =0
        
       
        for stone in stones:
            dic[stone] += 1
       
        # print(dic)
        for jewel in jewels:
            # print(jewel)
            # print(dic["A"])
            if jewel in dic:
                print(jewel)
                count += dic[str(jewel)]
        return count