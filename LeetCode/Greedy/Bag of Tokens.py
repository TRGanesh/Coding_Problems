'''
https://leetcode.com/problems/bag-of-tokens/description/

You start with an initial power of power, an initial score of 0, and a bag of tokens given as an integer array tokens, where each tokens[i] denotes the value of tokeni.

Your goal is to maximize the total score by strategically playing these tokens. In one move, you can play an unplayed token in one of the two ways (but not both for the same token):

Face-up: If your current power is at least tokens[i], you may play tokeni, losing tokens[i] power and gaining 1 score.
Face-down: If your current score is at least 1, you may play tokeni, gaining tokens[i] power and losing 1 score.
Return the maximum possible score you can achieve after playing any number of tokens.


'''

'''
- Maximum score can be achieved by taking maximum tokens
- So if we have less power than to get more power we have to use the score
- Then for incrementing the power we will choose such a token whose value is maximum
- Score is independent of the value of the token,, but power is dependent on the value of the token
'''
class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        n = len(tokens)
        
        i = 0
        j = n-1
        maxScore = 0
        score = 0

        # if tokens length is one
        if n == 1:
            if power >= tokens[0]:
                return 1
            else:
                return 0 

        if n > 0 and power < tokens[0]:
            return 0

        while i <= j:
            # Increment score if power is more than current token
            if power >= tokens[i]:
                score += 1
                maxScore = max(maxScore, score)
                power = power - tokens[i]
                i += 1

            # If no enough power then use the score to increase the power with Maximum valued token 
            if i < n and power < tokens[i]:
                power += tokens[j] # Adding power
                score -= 1 # Decrmenting score
                j -= 1 # Moving j pointer to left
                    
        return maxScore
          
