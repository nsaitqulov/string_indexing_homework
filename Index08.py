def main(s):
    """
    A string of length five is given. Return the index of the "*" character, return False if not present.
    Args:
        s(str): parameter
    Returns:
        int: answer
    """
    x=s.count("*")
    if x:
        return s.find("*")
    else:
        return x
    
print(main("244*"))
        