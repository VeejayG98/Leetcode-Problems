class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        freq = {}
        for card in hand:
            freq[card] = freq.get(card, 0) + 1
        no_of_cards = len(hand)
        hand = sorted(hand)

        for i in range(len(hand)):
            if freq[hand[i]] == 0:
                continue
            for j in range(1, groupSize):
                if hand[i] + j not in freq or freq[hand[i] + j] == 0:
                    return False
            for j in range(groupSize):
                freq[hand[i]+ j] -= 1
        
        return True
