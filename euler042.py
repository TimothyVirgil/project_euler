'''Solution to Project Euler Problem 41
Code by Timothy Virgil Payne Jr.
Started: 9/8/21
Completed: 9/8/21 '''

words = open("p042_words.txt",'r')

words_list = words.read().replace('"','').split(',')

tri_word_tot = 0

for a in words_list:
    curr_tri = 0

    for b in a:
        curr_tri += ord(b) - 64

    else:
        test_tri = 0
        n = 1

        while test_tri < curr_tri:
            test_tri = int(0.5*n*(n+1))
            n += 1

            if test_tri == curr_tri:
                tri_word_tot += 1

print(tri_word_tot)
            

