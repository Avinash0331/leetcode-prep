def remove_char(s, i, c):
    # Base case
    if i == len(s):
        return ""
    
    # Recursive call
    ans = remove_char(s, i + 1, c)

    # If current character matches → skip it
    if s[i] == c:
        return ans
    
    # Otherwise include it
    return s[i] + ans


# Example
print(remove_char("banana", 0, 'a'))   # bnn