#!/usr/bin/env python
msg_ = [
    "Enter an equation"
    , "Do you even know what numbers are? Stay focused!"
    , "Yes ... an interesting math operation. You've slept through all classes, haven't you?"
    ,  "Yeah... division by zero. Smart move..."
    , "Do you want to store the result? (y / n):"
    , "Do you want to continue calculations? (y / n):"
    , " ... lazy"
    , " ... very lazy"
    , " ... very, very lazy"
    , "You are"
    , "Are you sure? It is only one digit! (y / n)"
    , "Don't be silly! It's just one number! Add to the memory? (y / n)"
    , "Last chance! Do you really want to embarrass yourself? (y / n)"]

memory = 0


def is_one_digit(v):
    if type(v) == str:
        v = float(v)
    else:
        v = v
    if (-10) < v < 10 and v.is_integer():
        output = True
    else:
        output = False
    return output


def check(v_1, v_2, v_3):
    message = ""
    if is_one_digit(v_1) and is_one_digit(v_2):
        message = f"{message}{msg_[6]}"
    if (float(v_1) == 1 or float(v_2) == 1) and v_3 == "*":
        message = f"{message}{msg_[7]}"
    if (float(v_1) == 0 or float(v_2) == 0) and (v_3 == "*" or v_3 == "+" or v_3 == "-"):
        message = f"{message}{msg_[8]}"
    if message:
        message = f"{msg_[9]}{message}"
        print(message)


def user_input():
    global memory
    # print(memory)
    print(msg_[0])
    calc = input().strip()

    x, operation, y = calc.split(" ")

    if memory != 0:
        if x == "M":
            x = memory
            # print(x, type(x))
        if y == "M":
            y = memory
            # print(y, type(y))

    def check_digit(var_name):
        if len(str(var_name).split('.')) > 1:
            var_name = float(var_name)
        else:
            var_name = int(var_name)
        return var_name

    def is_not_digit(var_name, calc=calc):
        var_name = str(var_name)
        if var_name.isalpha():
            return True
        else:
            return False

    def ask_for_calc():
        print(msg_[5])
        answer = input()
        if answer == "y":
            user_input()
        elif answer == "n":
            return
        else:
            ask_for_calc()

    def print_msg(msg_index):
        print(msg_[msg_index])
        answer = input()
        if answer == "y":
            if msg_index < 12:
                msg_index += 1
                print_msg(msg_index)
            else:
                store_result(result)
        elif answer == "n":
            return
        else:
            print_msg(msg_index)

    def ask_for_store(result):
        print(msg_[4])
        answer = input()
        if answer == "y" and result != 0:
            if is_one_digit(result):
                msg_index = 10
                print_msg(msg_index)
            else:
                store_result(result)
            ask_for_calc()
        elif answer == "n":
            ask_for_calc()
        else:
            ask_for_store(result)

    def store_result(result):
        global memory
        memory = result
        return memory

    if is_not_digit(x) or is_not_digit(y):
        print(msg_[1])
        user_input()
    else:
        if operation == "+" or operation == "-" or operation == "*" or operation == "/":
            check(x, y, operation)
            if operation == "+":
                result = float(check_digit(x) + check_digit(y))
                print(result)
                ask_for_store(result)
            elif operation == "-":
                result = float(check_digit(x) - check_digit(y))
                print(result)
                ask_for_store(result)
            elif operation == "*":
                result = float(check_digit(x) * check_digit(y))
                print(result)
                ask_for_store(result)
            elif operation == "/" and check_digit(y) != 0:
                result = float(check_digit(x) / check_digit(y))
                print(result)
                ask_for_store(result)
            else:
                print(msg_[3])
                user_input()
        else:
            print(msg_[2])
            user_input()


user_input()
