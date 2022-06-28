'''Solution to Project Euler Problem 54
Code by Timothy Virgil Payne Jr.
Started: 6/2/22
Completed: 6/3/22
https://projecteuler.net/problem=54'''

card_value_map = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7,
                  '8': 8, '9': 9, 'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}


class Card:
    '''Class for a playing card'''

    def __init__(self, card_str: str):
        self.value = card_value_map[card_str[0]]
        self.card_str = card_str
        self.suit = card_str[1]

    def __str__(self):
        return self.card_str


class Hand:
    '''Five card hand'''

    def __init__(self, card_tuple: tuple[Card, Card, Card, Card, Card]):
        self.hand = card_tuple
        self.suits = tuple(x.suit for x in self.hand)
        self.values = tuple(sorted([x.value for x in self.hand]))
        self.hand_score = self.score_hand()

    def __str__(self):
        return str([x.card_str for x in self.hand])

    def __eq__(self, other):
        return (self.hand_score == other.hand_score
                and self.tiebreaker == other.tiebreaker)

    def __lt__(self, other):
        if self.hand_score < other.hand_score:
            return True

        elif self.hand_score == other.hand_score:
            if self.hand_score == other.hand_score:
                for x in range(1, len(self.tiebreaker)+1):
                    if self.tiebreaker[-x] < other.tiebreaker[-x]:
                        return True
                    elif self.tiebreaker[-x] == other.tiebreaker[-x]:
                        continue
                    else:
                        return False
                else:
                    return False

        else:
            return False

    def __gt__(self, other):
        if self.hand_score > other.hand_score:
            return True

        elif self.hand_score == other.hand_score:
            for x in range(1, len(self.tiebreaker)+1):
                if self.tiebreaker[-x] > other.tiebreaker[-x]:
                    return True
                elif self.tiebreaker[-x] == other.tiebreaker[-x]:
                    continue
                else:
                    return False
            else:
                return False

        else:
            False

    def score_hand(self):
        'iter through hands in order of value and assign score'
        if self.straight_flush() is not False:
            return self.straight_flush()

        elif self.four_of_kind() is not False:
            return self.four_of_kind()

        elif self.full_house() is not False:
            return self.full_house()

        elif self.flush() is not False:
            return self.flush()

        elif self.straight() is not False:
            return self.straight()

        elif self.three_of_kind() is not False:
            return self.three_of_kind()

        elif self.two_pair() is not False:
            return self.two_pair()

        elif self.pair() is not False:
            return self.pair()

        # high card
        else:
            self.tiebreaker = self.values
            return 1

    def straight_flush(self):
        if self.flush() is not False and self.straight() is not False:
            self.tiebreaker = self.values
            return 9
        else:
            return False

    def four_of_kind(self):
        for value in self.values:
            if self.values.count(value) == 4:
                self.tiebreaker = [value]
                return 8
            else:
                return False

    def full_house(self):
        if len(set(self.values)) == 2:
            self.tiebreaker = list(
                set([value for value in self.values
                     if self.values.count(value) == 3]))
            return 7
        else:
            return False

    def flush(self):
        if len(set(self.suits)) == 1:
            self.tiebreaker = self.values
            return 6
        else:
            return False

    def straight(self):
        if self.values == (2, 3, 4, 5, 14):
            self.tiebreaker = (1, 2, 3, 4, 5)
            return 5
        else:

            for x in range(1, 5):
                if self.values[x] - self.values[x-1] == 1:
                    continue
                else:
                    return False
            else:
                self.tiebreaker = self.values
                return 5

    def three_of_kind(self):
        for value in self.values:
            if self.values.count(value) == 3:
                self.tiebreaker = [value]
                return 4
            else:
                continue
        else:
            return False

    def two_pair(self):
        if len(set(self.values)) == 3:
            self.tiebreaker = [
                value for value in self.values
                if self.values.count(value) == 1]
            self.tiebreaker.extend(list(
                set((sorted([value for value in self.values
                             if self.values.count(value) == 2])))))
            return 3
        else:
            return False

    def pair(self):
        if len(set(self.values)) == 4:
            self.tiebreaker = list(
                sorted([value for value in self.values
                        if self.values.count(value) == 1]))
            self.tiebreaker.append(
                [value for value in self.values
                 if self.values.count(value) == 2][0])
            return 2
        else:
            return False


def poker_battle():

    with open('p054_poker.txt', ) as f:
        poker_hands = [line.strip().replace(' ', '') for line in f]

    player1_wins = 0
    player2_wins = 0

    for x in range(len(poker_hands)):
        player_1 = poker_hands[x][:10]
        player_2 = poker_hands[x][10:20]

        player_1 = tuple([Card(player_1[i:i+2]) for i in range(0, 10, 2)])
        player_2 = tuple([Card(player_2[i:i+2]) for i in range(0, 10, 2)])
        player_1 = Hand(player_1)
        player_2 = Hand(player_2)

        if player_1 > player_2:
            player1_wins += 1
        else:
            player2_wins += 1
    else:

        return player1_wins


if __name__ == '__main__':
    print(poker_battle())
