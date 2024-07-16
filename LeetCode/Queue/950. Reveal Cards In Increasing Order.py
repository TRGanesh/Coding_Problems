https://leetcode.com/problems/reveal-cards-in-increasing-order/description/

from collections import deque
class Solution:
def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        n = len(deck)
        # Queue contains the Indices
        queue = deque( range(0,n) )
        # Sorting the deck
        deck.sort()

        ans = [-1] * n # Ans

        deck_ptr = 0 # Pointer for deck
        while queue:
            idx = queue.popleft()
            ans[idx] = deck[deck_ptr
            deck_ptr += 1

            if queue: 
                next_idx = queue.popleft()
                queue.append(next_idx)
        
        return ans
