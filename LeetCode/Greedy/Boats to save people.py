https://leetcode.com/problems/boats-to-save-people/description/

class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        n = len(people)
        people.sort()

        i, j = 0, n-1
        
        numOfBoats = 0
        while i <= j:
            if people[i] + people[j] <= limit:
                numOfBoats += 1
                i += 1
                j -= 1
            
            elif people[i] + people[j] > limit:
                if people[j] <= limit:
                    numOfBoats += 1
                    j -= 1
        
        return numOfBoats
