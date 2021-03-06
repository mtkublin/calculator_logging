import logging
import sys
from functools import wraps

a_logger = logging.getLogger()
a_logger.setLevel(logging.DEBUG)

output_file_handler = logging.FileHandler("output.log")
stdout_handler = logging.StreamHandler(sys.stdout)

a_logger.addHandler(output_file_handler)
a_logger.addHandler(stdout_handler)


def input_data(func):

    @wraps(func)
    def wrapper():

        while True:

            numbers_list = input("Input number for calcualtion (in list separated with whitespace): ")
            print(numbers_list)
            try:
                numbers_list = [int(x) for x in numbers_list.split(' ')]
                if func == subtraction or division and len(numbers_list) > 2:
                    print("Can't process. Only two arguments accepted!!!")
                    continue
                else:
                    break
            except ValueError:
                print("Oops!  Podaj liczbę: ")
        func(numbers_list)
    return wrapper


@input_data
def addition(numbers_list):

    '''Adding number from list.
    User is asked to provide number separated only by whitespace.
    Example of correctly provided data: 12 2 3'''

    result = 0
    for number in numbers_list:
        a_logger.debug(f"Dodaje {number} do {result}")
        result = result + number

    return (result)

@input_data
def subtraction(numbers_list):

    '''Subtracting 2nd value from 1st value.
    Functin returns the result of subtraction.'''
    a_logger.debug(f"Odejmuje {numbers_list[0]} - {numbers_list[1]}")
    result = numbers_list[0] - numbers_list[1]
    return result


@input_data
def multiplication(numbers_list):

    '''Multiplying all values from a list.
    Function returns result of multiplication all number.'''

    result = 1

    for number in numbers_list:
        a_logger.debug(f"Mnoze {number} z {result}")
        result = int(number) * result
    return (result)

@input_data
def division(numbers_list):

    '''Dividing 2 provided by users number.
    Function return result of dividng 1st value by 2nd value.'''

    a_logger.debug(f"Dziele {numbers_list[0]} przez {numbers_list[1]}")
    result = numbers_list[0] / numbers_list[1]
    return(result)


if __name__ == "__main__":

    operation_dict = {
        1: addition,
        2: subtraction,
        3: multiplication,
        4: division
        }
    [print(key, value) for key, value in operation_dict.items()]

    calculation_type = int(input(f"Podaj działanie, posługując się odpowiednią liczbą: "))

    calculation = operation_dict.get(calculation_type)
    calculation()
