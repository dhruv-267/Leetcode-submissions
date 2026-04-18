class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand)%groupSize:
            return False
        ''' # O(n^2) solution : Easy
        while hand:
            mini = min(hand) 
            copy = hand.copy()
            for i in range(groupSize):
                if mini+i not in copy:
                    return False
                copy.remove(mini+i)
            hand = copy
        return True
        '''
        #T: O(n)  S: O(1) solution
        count = Counter(hand)

        for card in hand:
            start = card
            while count[start-1]:
                start-=1
            
            while start<=card:
                while count[start]:
                    for i in range(start,start+groupSize):
                        if not count[i]:
                            return False
                        count[i]-=1

                start+=1
        return True
   