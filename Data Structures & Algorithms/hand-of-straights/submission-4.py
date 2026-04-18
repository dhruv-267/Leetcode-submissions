class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand)%groupSize!= 0:
            return False
        count = Counter(hand)

        for card in hand:
            start = card
            while count[start-1]:
                start-=1
            while start<=card:
                while count[start]:
                    for c in range(start,start+groupSize):
                        if not count[c]:
                            return False
                        count[c]-=1
                start+=1

        return True




                    