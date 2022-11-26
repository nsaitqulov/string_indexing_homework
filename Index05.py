def main(s):
    """
    Given a variable s string of length five. Determine the number of digits involved in this variable.
    Args:
        s(str): parameter
    Returns:
        int: answer
    """
    x=s[0]
    x1=s[1]
    x2=s[2]
    x3=s[3]
    x4=s[4]

    a=0
    if x.isdigit():
        a+=1
    if x1.isdigit():
        a+=1
    if x2.isdigit():
        a+=1
    if x3.isdigit():
        a+=1
    if x4.isdigit():
        a+=1
    return a
print(main("32x3z"))