choice = "Y"

# Repeat program while user selects Y
while choice.upper() == "Y":

    # Input three quiz marks
    quiz_1 = float(input("Enter Quiz 1 mark: "))
    quiz_2 = float(input("Enter Quiz 2 mark: "))
    quiz_3 = float(input("Enter Quiz 3 mark: "))

    # Calculate average mark
    average = (quiz_1 + quiz_2 + quiz_3) / 3

    print("Average Mark =", average)

    # Check pass or fail
    if average >= 50:
        print("PASS")
    else:
        print("FAIL")

    # Ask user whether to continue
    choice = input("Continue? Select Y/N: ")

print("Program Ended")