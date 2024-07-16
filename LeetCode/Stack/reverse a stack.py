# Method 1 : Using Recursion + Auxiliary Space(Temporary Stack)
def solve(stack):
    if not stack:
        return
    
    # At first we store the top guy and pop it
    top_guy = stack[-1]
    stack.pop()
    
    # We call recursion for the remaining stack
    solve(stack)
    
    # After calling the recursive function the stack will be reversed
    # Now we have to add that stored top_guy at the bottom of this reversed stack
    # For that we will remove the things from the reversed stack and store them in an another temporary stack
    temp_stack = []
    # Using this is the temporary stack method not works for very large inputs
    
    while stack:
        temp_stack.append(stack[-1])
        stack.pop()
    
    stack.append(top_guy)
    # Again put the guys in the temporary stack in the original stack
    while temp_stack:
        stack.append(temp_stack[-1])
        temp_stack.pop()
    
    return stack
