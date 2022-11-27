def main(s,n):
    """
    The s string variable is given. n Return the character in the index, otherwise return False.
    Args:
        s(str): parameter
    Returns:
        str: answer
    """
    x=(len(s)-1)>=n
    if x:
        return s[n]
    else:
        return x
print(main("uz", 2))
    
