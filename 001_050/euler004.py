# Solution to Project Euler Problem 4
# Code by Tim Payne
# Completed: 04/04/2019

def Largest_Pal_Product():

    """
    This function is written to calculate the largest
    palindrome that is a product of two three digit numbers.

    999*999 = 998,001

    It is safe to assume our answer will be six digits.
    There will only be 100 palindromic numbers in each
    set of one-hundred thousand numbers.

    We can check each of these in reverse to find the first one that is
    a product of three-digit numbers.

    Overall, the code is more complicated than it needs to be but I defend my
    exploration of ways to make the algorithm more efficient."""

    for x in range(9,1,-1):

        for y in range(99,-1,-1):

            if y >= 10:

                poss_pal = str(x) + str(y) + str(y)[::-1] + str(x)

                num_pal = int(poss_pal)

                for z in range(int(num_pal**(1 /2)) + 1, 100, -1):

                    if num_pal % z == 0:

                        if num_pal // z > 100 and num_pal // z < 1000:

                            return num_pal

                        else:

                            break

                    else:

                        continue
            else:

                poss_pal = str(x) + str(0) + str(y) + str(y) + str(0) + str(x)

                num_pal = int(poss_pal)

                for z in range(int(num_pal**(1 /2)) + 1, 100, -1):

                    if num_pal % z == 0:

                        if num_pal // z > 100 and num_pal // z < 1000:

                            return num_pal

                        else:

                            break

                    else:

                        continue


   

if __name__ == '__main__':

    print(Largest_Pal_Product())


    

