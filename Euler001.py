# Solution to Project Euler Problem 1
# Code by Tim Payne
# Completed: 03/13/2019

def three_five_counter():

        solution = 0

        for a in range(1000):

                if a % 3 == 0 or a % 5 == 0:

                        solution += a

        print(solution)


if __name__ == '__main__':
        three_five_counter()









