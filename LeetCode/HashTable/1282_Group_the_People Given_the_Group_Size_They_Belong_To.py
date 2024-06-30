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
# Method 1
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

# -------------------------------------------------------------------------------------------------------
# Method 2
# In above Method, Splitting of Sub-Groups is done with many Condition Checks & a While Loop & Using Pointers
# We can also Simply find the Sub-Groups,, by Re-Slicing the Same List(Removing front "grpSize" numbered guys from list)

from collections import defaultdict
class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        groupSize_ids_map = defaultdict(list)
        
        for idx, grpSize in enumerate(groupSizes):
            groupSize_ids_map[grpSize].append(idx)
        
        groups = [] # Final Answer

        for grpSize, ids in groupSize_ids_map.items():
            while len(ids) >= grpSize:
                sub_grp = ids[ 0 : grpSize ]
                groups.append(sub_grp)

                # Let's update the List ids,, such that we can remove the 1st "grpSize" numbered people using Slicing
                ids = ids[ grpSize : ]

        return groups    

# -------------------------------------------------------------------------------------------------------
# Method 3
# In above 2 Methods, 1st we prepared the Map & then we performed the Splitting/Slicing Operations on Values of Map
# Can we do the Same when Buiding the Map ??

from collections import defaultdict
class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        groupSize_ids_map = defaultdict(list)
        groups = [] # Final Answer

        for idx, grpSize in enumerate(groupSizes):
            groupSize_ids_map[grpSize].append(idx)

            # Here,itself we can check the size of List(Value of Corresponding key) which is getting formed
            if len(groupSize_ids_map[grpSize]) == grpSize:
                groups.append(groupSize_ids_map[grpSize])

                # So, we appended the List into Final Ans
                # Then we have to Re-Initialize the Val of Corresponding Key to Empty List
                groupSize_ids_map[grpSize] = []

        return groups

# Final Thoughts
'''
- In method 1,, We did the Basic Operations for Splitting / Dividing the List into Parts of equal-sized
    - Those Operations includes,,
        --> Properly Checking the Size of List & comparing with Desired_Size 
        --> Finding the numOfDivisions, Using 2 Pointers for Slicing the ID's List(without Changing that List)
- In method 2,, We thought like,, We have a List & We want to break it into parts such that each part should have a desired size
    - So,, why don't we simply Do Re-Slicing the same List(Due to this List will update)
    - Such that at 1st we take k guys from front & Then We Re-Slice the List such that updated list will start from remaining guys
- In method 3,, We thought like,, Okay we are making the List(Value of Map) into parts,, whenever it's size equals to desiredSize
    - So,, Instead of Calculating for entire Array, Can't we break the List whenever we are Updating the Map
    - There Re-Initialization of Value is an important step
'''
            










      
