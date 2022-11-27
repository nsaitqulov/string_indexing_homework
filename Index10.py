def main(s):
    """
    A string of five numbers is given. Find the sum of its numbers.
    Args:
        s(str): parameter
    Returns:
        int: answer
    """
    if s.isdigit():
        x=int(s)

        a=x%10
        x//=10

        a1=x%10
        x//=10

        a2=x%10
        x//=10

        a3=x%10
        x//=10

        a4=x%10
        return a+a1+a2+a3+a4
print(main("12332"))