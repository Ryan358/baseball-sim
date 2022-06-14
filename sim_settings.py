"""Create classes, etc"""
import json
import random


class Ball:
    """what properties does a ball have? """

    def __init__(self, strike, hit, caught, live):
        self.strike = strike
        self.hit = hit
        self.caught = caught
        self.live = live

    def pitch(self):
        self.live = True
        if random.random() < 0.6:
            self.strike = True
        else:
            self.strike = False


class Player:

    def __init__(self, name, position, swung):
        self.name = name
        self.position = position
        self.swung = swung

    def at_bat(self, strike):
        strikes = 0
        balls = 0
        if random.random() < 0.5:
            print("Swing")
            self.swung = True
        else:
            print("Took the pitch.")
            self.swung = False
        if self.swung and strike:
            print("It's a hit!")
            return True
        elif self.swung and not strike:
            strikes += 1
        elif not self.swung and strike:
            strikes += 1
        elif not self.swung and not strike:
            balls += 1

        if strikes >= 3:
            print(f"Strike {strikes}, you're out!")


def create_roster(players: str):
    with open(players) as f:
        roster = json.load(f)
    for i in range(len(roster)):
        roster[i] = Player(roster[i]['name'], roster[i]['position'], None)
    return roster


def main():
    roster = create_roster("roster.json")
    print(roster[0].at_bat(True))


if __name__ == "__main__":
    main()
