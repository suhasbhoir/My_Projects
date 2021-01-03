def Add_Two_Num(num1, num2):
    return num1 + num2 + 50
def Take_Str(str):
    return f"Hi {str} plese provide your input here"

print(f"\nthese is {__name__}")

if __name__ == '__main__':
    strng = Take_Str("Suhas")
    print('\n',strng)
    addition = Add_Two_Num(10, 20)
    print("\nMy input is: ", addition, "\n")

    
    