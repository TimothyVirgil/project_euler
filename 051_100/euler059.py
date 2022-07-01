'''Solution to Project Euler Problem 59
Code by Timothy Virgil Payne Jr.
Started: 6/29/22
Completed: 6/29/22
https://projecteuler.net/problem=59
Using English words list from: https://github.com/dwyl/english-words

I tried to find some language processing libraries but none that I found
were any good at differentiating between English and gibberish. Interesting.

I wrote a hacky function that checks an English word list and ran it through
any possible messages that had the word 'the' in them 4 times.'''

from itertools import product
import path
import sys
directory = path.Path(__file__).abspath()
sys.path.append(directory.parent.parent)
from utils import timer


def is_english(text: str, words: list) -> bool:
    '''relies on imported english word dictionary'''
    word_list = text.replace(',', '')
    word_list = text.split(' ')
    words_in_dict = 0
    if len(word_list) < 20:
        return False
    for a in range(20):
        if word_list[a] in words:
            words_in_dict += 1
    if words_in_dict > 5:
        return True
    else:
        return False


@timer
def solve():

    words = open("p059_cipher.txt", 'r')
    words_list = words.read().split(',')
    words_list = list(map(lambda x: int(x), words_list))
    eng_file = open("words.txt", 'r')
    eng_words = eng_file.read().split('\n')
    eng_file.close()

    poss_keys = product(list(range(97, 123)), repeat=3)

    for key in poss_keys:

        decode_text = ''
        key = (101, 120, 112)
        code_sum = 0
        for a in range(0, len(words_list), 3):
            ord1 = words_list[a] ^ key[0]
            ord2 = words_list[a+1] ^ key[1]
            ord3 = words_list[a+2] ^ key[2]
            let1 = chr(ord1)
            let2 = chr(ord2)
            let3 = chr(ord3)
            code_sum += (ord1 + ord2 + ord3)
            decode_text += (let1 + let2 + let3)

        if decode_text.count('the') > 4:
            if is_english(decode_text, eng_words):
                return (decode_text, code_sum)

    else:
        return 'No message found!'


if __name__ == '__main__':
    ans = solve()
    print('\nMessage: ', ans[0])
    print('\nsum: ', ans[1], '\n')
