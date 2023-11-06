#print("here is my second python program whcih demonstrates print function again")


def function_name(variable_1, variable_2):
    # TODO: Logic
    return


def addition(input_1, input_2):
    return input_1 + input_2

def build_full_name(first_name, last_name):
    name = first_name + " " + last_name
    return name



if __name__ == "__main__":
    number_1 = 4
    number_2 = 3
    print(type(number_1))
    print(type(number_2))
    addition_of_two_values = addition(number_1, number_2)
    print(f"Addition of {number_1} and {number_2} values is {addition_of_two_values}")


    first_name = "Aviral"
    last_name = "Vishnoi"

    full_name = build_full_name(first_name, last_name)
    print(f"Concatenation of {first_name} and {last_name} is: {full_name}")