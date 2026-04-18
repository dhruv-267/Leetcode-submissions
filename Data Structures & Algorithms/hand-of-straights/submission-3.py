class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand)%groupSize!= 0:
            return False

        hand.sort()
        hashmap = {}
        for card in hand:
            hashmap[card] = 1 + hashmap.get(card,0)
        
        for card in hand:
            while hashmap[card]!=0:
                for i in range(groupSize):
                    if not hashmap.get(card+i,0):
                        return False
                    else:
                        hashmap[card+i]-=1
        return True
                    