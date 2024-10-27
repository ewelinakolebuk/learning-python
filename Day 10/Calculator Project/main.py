from art import logo
print(logo)
def add(n1, n2):
    print(f"{n1} + {n2} = {n1+n2}")
    return n1 + n2
def subtract(n1, n2):
    print(f"{n1} - {n2} = {n1 - n2}")
    return n1 - n2
def multiply (n1, n2):
    print(f"{n1} * {n2} = {n1 * n2}")
    return n1 * n2
def divide(n1, n2):
    print(f"{n1} / {n2} = {n1 / n2}")
    return n1 / n2

operation = {
    "+":add,
    "-":subtract,
    "*":multiply,
    "/":divide,
}
#print(operation["*"](4,8))
while True:
    should_accumulate = True
    first_number= float(input("What is the first number?: "))
    while should_accumulate:
        print("+ \n-\n*\n/")
        chosen_operation=input("Pick an operation: ")
        second_number=float(input("What is the second number?: "))
        for key in operation:
            if key == chosen_operation:
                result = operation[chosen_operation](first_number,second_number)
        y_or_n = input(f"Type 'y' to continue calculating with {result}, or 'n' to start a new calculation: ")
        if y_or_n=="y":
            first_number=result
        else:
            should_accumulate=False


#TODO If yes, program loops to use the previous result as the first number and then repeats the calculation process.
#TODO If no, program asks the user for the fist number again and wipes all memory of previous calculations.