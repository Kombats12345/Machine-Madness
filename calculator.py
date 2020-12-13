import random
suffix = 0


def st_nd_rd_th(number):
    global suffix
    if float(str(number)[len(str(number)) - 1]) == 1:
        suffix = "st"
    elif float(str(number)[len(str(number)) - 1]) == 2:
        suffix = "nd"
    elif float(str(number)[len(str(number)) - 1]) == 3:
        suffix = "rd"
    else:
        suffix = "th"


def isfloat(will_it_float):
    try:
        float(will_it_float)
        return True
    except ValueError:
        return False


seed = random.randint(38, 62)


class Certainty:
    add = seed
    subtract = seed
    multiply = seed
    divide = seed
    power = seed
    root = seed


while True:
    class Operation:
        add = [0]
        subtract = [0]
        multiply = [0]
        divide = [0]
        power = [0]
        root = [0]


    num = [0]
    num_1 = input("\nGive me a number: ")
    while isfloat(num_1) is False:
        num_1 = input("\nNo, try again.\n\nGive me a number: ")
    num_1 = float(num_1)
    operation = 0
    num_2 = input("\nGive me the next number: ")
    while isfloat(num_2) is False:
        num_2 = input("\nNo, try again.\n\nGive me a number: ")
    num_2 = float(num_2)
    st_nd_rd_th(number=num_2)
    while operation == 0:
        operation = input("Type \"+\" to add them.\nType \"-\" to subtract them.\nType \"*\" to multiply them.\nType \"/\" to divide them respectively.\nType \"^\" for " + str(num_1) + " to the " + str(num_2) + suffix + " power.\nType \"//\" for the " + str(num_2) + suffix + " root of " + str(num_1) + ".\nType \"random\" for a random operation.\nType \"exit\" or \"quit\" to leave.\n")
        if operation.lower() == "random":
            operation_rng = random.randint(0, 5)
            if operation_rng == 0:
                operation = "+"
                print("\nThe operation chosen was addition.")
            if operation_rng == 1:
                operation = "-"
                print("\nThe operation chosen was subtraction.")
            if operation_rng == 2:
                operation = "*"
                print("\nThe operation chosen was multiplication.")
            if operation_rng == 3:
                operation = "/"
                print("\nThe operation chosen was division.")
            if operation_rng == 4:
                operation = "^"
                print("\nThe operations chosen were exponents.")
            if operation_rng == 5:
                operation = "//"
                print("\nThe operations chosen were roots.")
        elif operation not in ["+", "-", "*", "/", "^", "//"] and operation.lower() not in ["exit", "quit"]:
            print("No, try again.\n")
            operation = 0
    if operation == "+":
        solution = num_1 + num_2
        Operation.add.append(1)
    elif operation == "-":
        solution = num_1 - num_2
        Operation.subtract.append(1)
    elif operation == "*":
        solution = num_1 * num_2
        Operation.multiply.append(1)
    elif operation == "/":
        if num_2 == 0:
            solution = "undefined"
            print("\nYou can't do that!\n")
        else:
            solution = num_1 / num_2
            Operation.divide.append(1)
    elif operation == "^":
        solution = pow(num_1, num_2)
        Operation.power.append(1)
    elif operation == "//":
        if num_2 == 0:
            solution = "undefined"
            print("\nYou can't do that!\n")
        else:
            solution = pow(num_1, 1 / num_2)
            Operation.root.append(1)
    elif operation.lower() == "exit":
        exit()
    elif operation.lower() == "quit":
        quit()
    print("\nThe solution is " + str(solution) + "!")
    if solution != "undefined":
        num.append(num_1)
        num.append(num_2)
        num_1 = solution
        if num[1] == 2 and num[2] == 2 and solution == 4:
            if Certainty.add > Certainty.multiply and Certainty.add > Certainty.power:
                print("I'm not too sure, but I think addition was used.\n")
                if 1 in Operation.add:
                    print("I'm correct!")
                    Certainty.add = Certainty.add * 98.5 / 99 + 50 / 99
                else:
                    print("I'm wrong....")
                    Certainty.multiply = Certainty.multiply * 74.25 / 99
            elif Certainty.multiply > Certainty.add and Certainty.multiply > Certainty.power:
                print("I'm not too sure, but I think multiplication was used.\n")
                if 1 in Operation.multiply:
                    print("I'm correct!")
                    Certainty.multiply = Certainty.multiply * 98.5 / 99 + 50 / 99
                else:
                    print("I'm wrong....")
                    Certainty.multiply = Certainty.multiply * 74.25 / 99
            elif Certainty.power > Certainty.add and Certainty.power > Certainty.multiply:
                print("I'm not too sure, but I think exponents were used.\n")
                if 1 in Operation.power:
                    print("I'm correct!")
                    Certainty.power = Certainty.power * 98.5 / 99 + 50 / 99
                else:
                    print("I'm wrong....")
            else:
                print("I'm not sure whether addition, multiplication, or exponents were used, but I know that only one of them was used.\n")
        elif num[1] == 1 and num[2] == 1 and solution == 1 or num[2] == 1 and solution == num[1]:
            if Certainty.multiply > Certainty.divide and Certainty.multiply > Certainty.power and Certainty.multiply > Certainty.root:
                print("I'm not too sure, but I think multiplication was used.\n")
                if 1 in Operation.multiply:
                    print("I'm correct!")
                    Certainty.multiply = Certainty.multiply * 98.5 / 99 + 50 / 99
                else:
                    print("I'm wrong....")
                    Certainty.multiply = Certainty.multiply * 74.25 / 99
            elif Certainty.divide > Certainty.multiply and Certainty.divide > Certainty.power and Certainty.divide > Certainty.root:
                print("I'm not too sure, but I think division was used.\n")
                if 1 in Operation.divide:
                    print("I'm correct!")
                    Certainty.divide = Certainty.divide * 98.5 / 99 + 50 / 99
                else:
                    print("I'm wrong....")
                    Certainty.divide = Certainty.divide * 74.25 / 99
            elif Certainty.power > Certainty.multiply and Certainty.power > Certainty.divide and Certainty.power > Certainty.root:
                print("I'm not too sure, but I think exponents were used.\n")
                if 1 in Operation.power:
                    print("I'm correct!")
                    Certainty.power = Certainty.power * 98.5 / 99 + 50 / 99
                else:
                    print("I'm wrong....")
                    Certainty.power = Certainty.power * 74.25 / 99
            elif Certainty.root > Certainty.multiply and Certainty.root > Certainty.divide and Certainty.root > Certainty.power:
                print("I'm not too sure, but I think roots were used.\n")
                if 1 in Operation.root:
                    print("I'm correct!")
                    Certainty.root = Certainty.root * 98.5 / 99 + 50 / 99
                else:
                    print("I'm wrong....")
                    Certainty.root = Certainty.root * 74.25 / 99
            else:
                print("I'm not sure whether multiplication, division, exponents, or roots were used, but I know that only one of them was used.\n")
        elif num[1] == 0 and num[2] == 0 and solution == 0:
            if Certainty.add > Certainty.multiply and Certainty.add > Certainty.subtract and Certainty.add > Certainty.power:
                print("I'm not too sure, but I think addition was used.\n")
                if 1 in Operation.add:
                    print("I'm correct!")
                    Certainty.add = Certainty.add * 98.5 / 99 + 50 / 99
                else:
                    print("I'm wrong....")
                    Certainty.add = Certainty.add * 74.25 / 99
            elif Certainty.subtract > Certainty.add and Certainty.subtract > Certainty.multiply and Certainty.subtract > Certainty.power:
                print("I'm not too sure, but I think subtraction was used.\n")
                if 1 in Operation.subtract:
                    print("I'm correct!")
                    Certainty.subtract = Certainty.subtract * 98.5 / 99 + 50 / 99
                else:
                    print("I'm wrong....")
                    Certainty.subtract = Certainty.subtract * 74.25 / 99
            elif Certainty.multiply > Certainty.add and Certainty.multiply > Certainty.subtract and Certainty.multiply > Certainty.power:
                print("I'm not too sure, but I think multiplication was used.\n")
                if 1 in Operation.multiply:
                    print("I'm correct!")
                    Certainty.multiply = Certainty.multiply * 98.5 / 99 + 50 / 99
                else:
                    print("I'm wrong....")
                    Certainty.multiply = Certainty.multiply * 74.25 / 99
            elif Certainty.power > Certainty.add and Certainty.power > Certainty.subtract and Certainty.power > Certainty.multiply:
                print("I'm not too sure, but I think exponents were used.\n")
                if 1 in Operation.power:
                    print("I'm correct!")
                    Certainty.power = Certainty.power * 98.5 / 99 + 50 / 99
                else:
                    print("I'm wrong....")
                    Certainty.power = Certainty.power * 74.25 / 99
            else:
                print("I'm not sure whether addition, subtraction, multiplication, or exponents were used, but I know that only one of them was used.\n")
        elif num[1] + num[2] == solution:
            print("I think addition was used.\n")
            if 1 in Operation.add:
                print("I'm correct!")
                Certainty.add = Certainty.add * 98.5 / 99 + 50 / 99
            else:
                print("I'm wrong....")
                Certainty.add = Certainty.add * 74.25 / 99
        elif num[1] - num[2] == solution:
            print("I think subtraction was used.\n")
            if 1 in Operation.subtract:
                print("I'm correct!")
                Certainty.subtract = Certainty.subtract * 98.5 / 99 + 50 / 99
            else:
                print("I'm wrong....")
                Certainty.subtract = Certainty.subtract * 74.25 / 99
        elif num[1] * num[2] == solution:
            print("I think multiplication was used.\n")
            if 1 in Operation.multiply:
                print("I'm correct!")
                Certainty.multiply = Certainty.multiply * 98.5 / 99 + 50 / 99
            else:
                print("I'm wrong....")
                Certainty.multiply = Certainty.multiply * 74.25 / 99
        elif num[2] != 0 and num[1] / num[2] == solution:
            print("I think division was used.\n")
            if 1 in Operation.divide:
                print("I'm correct!")
                Certainty.divide = Certainty.divide * 98.5 / 99 + 50 / 99
            else:
                print("I'm wrong....")
                Certainty.divide = Certainty.divide * 74.25 / 99
        elif num[2] != 0 and pow(num[1], 1 / num[2]) == solution:
            print("I think roots were used.\n")
            if 1 in Operation.root:
                print("I'm correct!")
                Certainty.root = Certainty.root * 98.5 / 99 + 50 / 99
            else:
                print("I'm wrong....")
                Certainty.root = Certainty.root * 74.25 / 99
        elif pow(num[1], num[2]) == solution:
            print("I think exponents were used.\n")
            if 1 in Operation.power:
                print("I'm correct!")
                Certainty.power = Certainty.power * 98.5 / 99 + 50 / 99
            else:
                print("I'm wrong....")
                Certainty.power = Certainty.power * 74.25 / 99
        else:
            print("I'm not sure how many times each operation was used....")
        if sum(Operation.add) > sum(Operation.subtract) and sum(Operation.add) > sum(Operation.multiply) and sum(Operation.add) > sum(Operation.divide) and sum(Operation.add) > sum(Operation.power) and sum(Operation.add) > sum(Operation.root):
            Certainty.add = Certainty.add * 98.75 / 99 + 25 / 99
        elif sum(Operation.subtract) > sum(Operation.add) and sum(Operation.subtract) > sum(Operation.multiply) and sum(Operation.subtract) > sum(Operation.divide) and sum(Operation.subtract) > sum(Operation.power) and sum(Operation.subtract) > sum(Operation.root):
            Certainty.subtract = Certainty.subtract * 98.75 / 99 + 25 / 99
        elif sum(Operation.multiply) > sum(Operation.add) and sum(Operation.multiply) > sum(Operation.subtract) and sum(Operation.multiply) > sum(Operation.divide) and sum(Operation.multiply) > sum(Operation.power) and sum(Operation.multiply) > sum(Operation.root):
            Certainty.multiply = Certainty.multiply * 98.75 / 99 + 25 / 99
        elif sum(Operation.divide) > sum(Operation.add) and sum(Operation.divide) > sum(Operation.subtract) and sum(Operation.divide) > sum(Operation.multiply) and sum(Operation.divide) > sum(Operation.power) and sum(Operation.divide) > sum(Operation.root):
            Certainty.divide = Certainty.divide * 98.75 / 99 + 25 / 99
        elif sum(Operation.power) > sum(Operation.add) and sum(Operation.power) > sum(Operation.subtract) and sum(Operation.power) > sum(Operation.multiply) and sum(Operation.power) > sum(Operation.divide) and sum(Operation.power) > sum(Operation.root):
            Certainty.power = Certainty.power * 98.75 / 99 + 25 / 99
        elif sum(Operation.root) > sum(Operation.add) and sum(Operation.root) > sum(Operation.subtract) and sum(Operation.root) > sum(Operation.multiply) and sum(Operation.root) > sum(Operation.divide) and sum(Operation.root) > sum(Operation.power):
            Certainty.root = Certainty.root * 98.75 / 99 + 25 / 99
