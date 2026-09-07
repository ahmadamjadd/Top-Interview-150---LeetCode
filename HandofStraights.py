from collections import Counter
from typing import List

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
            
        count = Counter(hand)
        
        for card in sorted(count.keys()):
            if count[card] > 0:
                needed_straights = count[card]
                
                for i in range(card, card + groupSize):
                    if count[i] < needed_straights:
                        return False
                    
                    count[i] -= needed_straights
                    
        return True
