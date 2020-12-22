import sys
from collections import deque
import numpy as np

class Player():
    def __init__(self, id, deck):
        self.id = id
        self.deck = deque(deck)

    def __str__(self):
        return f'<Player({self.id}, {self.deck})>'

    def __repr__(self):
        return str(self)

    def play_card(self):
        return self.deck.popleft()

    def add_card(self, card):
        self.deck.append(card)

    def has_cards(self):
        return len(self.deck) > 0

def get_input():
    with open(sys.argv[2], 'r') as f:
        state = 0
        for line in f:
            line = parse_line(line)
            if state == 0:
                id = int(line[7:-1])
                deck = list()
                state = 1
            elif state == 1:
                if line == '':
                    state = 0
                    yield Player(id, deck)
                else:
                    deck.append(int(line))
        yield Player(id, deck)


def parse_line(line):
    return line.strip()

def calculate_score(player):
    deck_size = len(player.deck)
    return sum((deck_size - i) * element for i, element in enumerate(player.deck))

def part1():
    players = list(get_input())
    while all(player.has_cards() for player in players):
        played_cards = [player.play_card() for player in players]
        winner = np.argmax(played_cards)
        for card in sorted(played_cards, reverse=True):
            players[winner].add_card(card)

    return max(calculate_score(player) for player in players)

previous_states = set()

def part2():
    players = list(get_input())
    while all(player.has_cards() for player in players):
        played_cards = [player.play_card() for player in players]
        winner = np.argmax(played_cards)
        for card in sorted(played_cards, reverse=True):
            players[winner].add_card(card)

    return max(calculate_score(player) for player in players)

if __name__ == '__main__':
    if sys.argv[1] == '1':
        print(part1())
    elif sys.argv[1] == '2':
        print(part2())
