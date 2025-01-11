def calculator(num1, num2, operation):
    if operation == 1:
        return num1 + num2
    elif operation == 2:
        return num1 - num2
    elif operation == 3:
        return num1 * num2
    elif operation == 4:
            try:
                return num1 / num2
            except Exception as e:
               print(e)
    elif operation == 5:
        if num2 == 0:
            return "Error: Modulus by zero"
        return num1 % num2
    else:
        return "No valid operation selected"
    
def main():
    while True:
        num1 = float(input("Enter num1: "))
        num2 = float(input("Enter num2: "))
        operation = int(input("Enter an operation: "))
        ans = calculator(num1, num2, operation)
        print(ans)
        again = input("Are you sure to recalculate: yes/no").lower()
        if again != "yes":
            break 
        
if __name__=="__main__":
    main()
