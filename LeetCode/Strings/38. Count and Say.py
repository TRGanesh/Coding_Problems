https://leetcode.com/problems/count-and-say/

def countAndSay(self, n: int) -> str:
    def solve(n):
        # Base Case
        if n == 1:
            return '1'

        # We will Call for the remaining
        say = solve(n-1)

        # Next we have to Process that "say"
        # We have to get the Frequencies as the Sequence goes on
        i,j = 0,1
        cnt = 1
        ans = ""
        while i < len(say) and j <= len(say):
            while i < len(say) and j < len(say) and say[i] == say[j]:
                cnt += 1 
                j += 1
            
            ans = ans + str(cnt) + say[i] # Updating Answer with Freq & Character

            i = j
            j = j + 1
            cnt = 1
        
        return ans

    return solve(n)
    
