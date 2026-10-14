
# Name: Mariem Cisse
# Course: IS 211
# Assignment: 7 - Pig Game

import random


class Player:
def __init__(self, name):
self.name = name
self.score = 0


class PigGame:
def __init__(self):
self.players = [Player("Player 1"), Player("Player 2")]

def play(self):
print("Welcome to the Pig Game!")
current = 0

while True:
player = self.players[current]
turn_total = 0
print(f"\n{player.name}'s turn. Score: {player.score}")

while True:
choice = input("Roll or hold? (r/h): ").lower().strip()

if choice == "h":
player.score += turn_total
break
elif choice == "r":
roll = random.randint(1, 6)
print("You rolled:", roll)

if roll == 1:
turn_total = 0
print("Turn over!")
break

turn_total += roll
print("Turn total:", turn_total)

if player.score + turn_total >= 100:
player.score += turn_total
print(f"{player.name} wins with {player.score} points!")
return
else:
print("Enter r to roll or h to hold.")

if player.score >= 100:
print(f"{player.name} wins!")
return

print("Scores:", self.players[0].score, "-", self.players[1].score)
current = (current + 1) % 2


if __name__ == "__main__":
game = PigGame()
game.play()
