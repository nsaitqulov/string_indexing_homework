def main(s):
    """
    A string of length five is given. Return the index of the "*" character, return False if not present.
    Args:
        s(str): parameter
    Returns:
        int: answer
    """
    x=s.find("*",0,(len(s)+1))
    y=x=="*"
    if y:
        return s.index("*")
    else :
        return y

print(main("good"))
        