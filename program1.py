class Solution(object):
def isValid(s: str) -> bool:
    # Stack to keep track of opening brackets
    stack = []
    
    # Hash map to maintain the mappings for valid parentheses
    mapping = {')': '(', '}': '{', ']': '['}
    
    # Loop through each character in the input string
    for char in s:
        # If the character is a closing bracket
        if char in mapping:
            # Pop the topmost element from the stack, if it's non-empty; otherwise assign a dummy value
            top_element = stack.pop() if stack else '#'
            
            # If the topmost element doesn't match the corresponding opening bracket, return False
            if mapping[char] != top_element:
                return False
        else:
            # It's an opening bracket, so push it onto the stack
            stack.append(char)
    
    # If the stack is empty, it means all brackets were matched; otherwise, some were left unmatched
    return not stack
        pass







    



  

