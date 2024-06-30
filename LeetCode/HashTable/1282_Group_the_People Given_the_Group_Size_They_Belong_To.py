'''
Problem Link : https://leetcode.com/problems/group-the-people-given-the-group-size-they-belong-to/description/

There are n people that are split into some unknown number of groups. Each person is labeled with a unique ID from 0 to n - 1.

You are given an integer array groupSizes, where groupSizes[i] is the size of the group that person i is in. For example, if groupSizes[1] = 3, then person 1 must be in a group of size 3.

Return a list of groups such that each person i is in a group of size groupSizes[i].

Each person should appear in exactly one group, and every person must be in a group. If there are multiple answers, return any of them. It is guaranteed that there will be at least one valid solution for the given input.

Example 1:
  
Input: groupSizes = [3,3,3,3,3,1,3]
Output: [[5],[0,1,2],[3,4,6]]
Explanation: 
The first group is [5]. The size is 1, and groupSizes[5] = 1.
The second group is [0,1,2]. The size is 3, and groupSizes[0] = groupSizes[1] = groupSizes[2] = 3.
The third group is [3,4,6]. The size is 3, and groupSizes[3] = groupSizes[4] = groupSizes[6] = 3.
Other possible solutions are [[2,1,6],[5],[0,4,3]] and [[5],[0,6,2],[4,3,1]].

Example 2:

Input: groupSizes = [2,1,3,3,3,2]
Output: [[1],[0,5],[2,3,4]]
'''

''' ******************************* CODE WITH EXPLANATIN *********************************
- Unique ID means Just Index
- Each Value Represents the Group-Size to which that ID th guy is belongs to
- We have to create a List of List,, which contains the ID's of the People with Same GroupSize

Ex : groupSizes = [2,1,3,3,3,2]
    --> No. of People with GroupSize = 1 are 1,,Id's List is [1]
    --> No. of People with GroupSize = 2 are 2,,Id's List is [0,5]
    --> No. of People with GroupSize = 3 are 3,,Id's List is [2,3,4]

- So, we can Simply use a Map,, where Key wil be Exact GroupSize & Value will be a List of IDs(Indices)
- Now, If len(List of Id's) > GroupSize,, then we have to Break that List into parts such that each part has GroupSize guys

Ex: groupSizes = [3,3,3,3,3,1,3]
    --> No. of People with GroupSize = 3 are 6,,Id's List is [0,1,2,3,4,6]
    --> Now, we just have to break that List into parts,, where each part has size = GroupSize i.e 3
    --> [0,1,2],[3,4,6]
'''
from collections import defaultdict
class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        groupSize_ids_map = defaultdict(list)
        
        for idx, grpSize in enumerate(groupSizes):
            groupSize_ids_map[grpSize].append(idx)
        
        groups = [] # Final Answer

        for grpSize, ids in groupSize_ids_map.items():
            # Here grpSize will be the Size of Group
            # ids is List of ID's             
            numOfPeople = len(ids)

            if numOfPeople <= grpSize:
                # Ex: No. of People with GroupSize = 2 are 2,,Id's List is [0,5]
                # Then Simply Append that List into Final Answer
                groups.append(ids)

            elif grpSize == 1 and numOfPeople > 1:
                # Ex: No. of People with GroupSize = 1 are 3,,Id's List is [0,2,3]
                # Then we have to make 3 Lists --> [0],[2],[3]
                for i in range(numOfPeople):
                    groups.append( [ids[i]] )

            elif numOfPeople % grpSize == 0:
                # Ex : No. of People with GroupSize = 3 are 6,,Id's List is [0,1,2,3,4,6]

                # Let's Get Number of Parts/Divisions to make
                numOfDivisions = (numOfPeople // grpSize)

                # Using 2 Points for Slicing 
                ptr1, ptr2 = 0, grpSize
                while numOfDivisions:
                    sub_grp = ids[ ptr1 : ptr2 ] # sub_grp has exactly "grpSize" number of people 
                    groups.append(sub_grp)                    

                    # Updating the Pointers,, such that they should point to Next Part/Division
                    ptr1 = ptr2
                    ptr2 = ptr2 + grpSize

                    numOfDivisions -= 1

        return groups
