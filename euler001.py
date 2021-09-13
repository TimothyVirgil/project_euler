''' Solution to Project Euler Problem 1
 Code by Tim Payne
 Completed: 03/13/2019'''

def three_five_counter():

    "Count the multiples of 3 and 5"

    solution = 0

    for num in range(1000):
        if num % 3 == 0 or num % 5 == 0:
            solution += num

        print(solution)


if __name__ == '__main__':
    three_five_counter()
