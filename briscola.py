import random

class Card:
    def __init__(self, seed, number, value):
        self.seed = seed
        self.number = number
        self.value = value

class Player:
    def __init__(self, name, hand, inventory):
        self.name = name
        self.hand = hand
        self.inventory = inventory

def get_value(number):
    if number == 'asso': return 11
    elif number == '3': return 10
    elif number == 're': return 4
    elif number == 'cavallo': return 3
    elif number == 'donna': return 2
    else: return 0

def get_hand_winner(cards, briscola):
    if cards[0].seed == cards[1].seed:
        if cards[0].value > cards[1].value:
            return 0
        elif cards[0].value < cards[1].value:
            return 1
        elif cards[0].value == cards[1].value:
            return cards[0].index(number) < cards[1].index(number)
    elif cards[0].seed != cards[1].seed:
        return 0
    elif cards[0].seed == briscola.seed and cards[1].seed != briscola.seed:
        return 0
    elif cards[0].seed != briscola.seed and cards[1].seed == briscola.seed:
        return 1

players = ['', '']

for i in range(len(players)):
    players[i] = Player(input(f"Nome giocatore {i + 1}: "), [], [])

seeds = ['denari', 'coppe', 'spade', 'bastoni']
numbers = ['asso', '2', '3', '4', '5', '6', '7', 'donna', 'cavallo', 're']

deck = []
ground = []

for s in seeds:
    for n in numbers:
        deck.append(Card(s, n, get_value(n)))

random.shuffle(deck)
briscola = deck[-1]
print(f"\n\nBriscola: {briscola.number} di {briscola.seed}\n")

for p in players:
    print(f"{p.name}:")
    for j in range(3):
        p.hand.append(deck[0])
        print(f"{deck[0].number} di {deck[0].seed}")
        deck.remove(deck[0])

while len(deck) > 0:
    for p in players:
        print(f"{p.name}:")

        for c in p.hand:
            print(f"{c.number} di {c.seed} (valore: {c.value})")

        play = 0

        while True:
            try:
                play = int(input("Posizione della carta da giocare (1, 2, 3):"))
                if not (play > 0 and play <= len(p.hand)):
                    raise Exception("Numero non valido")
                break
            except:
                print("Inserisci un numero valido")

        play = play - 1

        ground.append(p.hand[play])
        print(f"\n{p.name} gioca {p.hand[play].number} di {p.hand[play].seed}\n")
        del p.hand[play]

        if len(ground) == 2:
            print(f"Vince la presa {players[get_hand_winner(ground, briscola)].name}")
            ground = []

        if get_hand_winner == 1:
            pass
