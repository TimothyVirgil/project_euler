import itertools

bozo=12345

clown=str(bozo)

def longestWord(letters):
    return [''.join(i) for i in itertools.permutations(letters)]

jokelist=longestWord(clown)

print(jokelist)
