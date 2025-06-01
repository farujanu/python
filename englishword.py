number_to_word={
    0:"zero",
    1:"one",
    2:"two",
    3:"three",
    4:"four",
    5:"five",
    6:"six",
    7:"seven",
    8:"eight",
    9:"nine"
    }
num=int(input("enter a single-digit number(0-9):"))
if 0 <=num <=9:
        print(f"the number in words is:{number_to_word[num]}")
else:
        print("invalid input! please enter a numbrer between 0 and 9,")
