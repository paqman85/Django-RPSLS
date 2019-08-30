import random

moves = [
    "Rock",
    "Paper",
    "Scissors",
    "Lizard",
    "Spock",
]

winner = "You are the Winner!"
loser = "You are the loser!"
champion = "TBD"

def Rock(pl2):
    if pl2 == "Scissors" or "Rock":
        return winner
    else:
        return loser

def Paper(pl2):
    if pl2 == "Rock" or "Spock":
        return winner
    else:
        return loser

def Scissors(pl2):
    if pl2 == "Paper" or "Lizard":
        return winner
    else:
        return loser

def Lizard(pl2):
    if pl2 == "Paper" or "Spock":
        return winner
    else:
        return loser

def Spock(pl2):
    if pl2 == "Rock" or "Scissors":
        return winner
    else:
        return loser



def cpuChoice():
    choice = moves[(random.randrange(0,4))]
    return choice

def bestof5Check(pl1Score,pl2Score):
    if pl1Score > 3:
        champion="Player 1"
    elif pl2Score > 3:
        champion="Player 2"
    return champion

