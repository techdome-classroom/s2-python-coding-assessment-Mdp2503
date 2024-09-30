class Solution(object):
    def romanToInt(self, s):

        # Dictionary to map Roman numerals to their corresponding integer values
        roman_map = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50, 
            'C': 100, 'D': 500, 'M': 1000
        }
        
        # Initialize result variable
        result = 0
        
        # Traverse through the string of Roman numerals
        for i in range(len(s)):
            # If the current numeral is less than the next one, subtract it from the result
            if i < len(s) - 1 and roman_map[s[i]] < roman_map[s[i + 1]]:
                result -= roman_map[s[i]]
            else:
                # Otherwise, add its value to the result
                result += roman_map[s[i]]
        
        return result
        pass



