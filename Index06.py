def main(s):
    """
    A string variable consisting of several characters is given. Add and return the first and last character.
    Args:
        s(str): parameter
    Returns:
        str: answer
    """
    x=s[0]
    y=s[-1]
    return x+y
print(main("good"))