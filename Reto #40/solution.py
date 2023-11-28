def multiply_table(number: int) -> str:
    """
        Create a multiply table based in a number given by the user.
        :param number: int number
        :return string of the multiply table 
    """
    for i in range(1, 11):
        print(f"{number} x {i} = {number*i}")

print("Select a number")
number = int(input())
multiply_table(number)