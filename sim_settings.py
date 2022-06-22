"""Create classes, etc"""
import json
import random


class Ball:
    """Create a ball object with a strike, hit, caught, and live status"""

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
    """Create a player class with a name, position, swung, strikes, and out status"""

    def __init__(self, name, number, position, swung, strikes, balls, hit, out, walked):
        self.name = name
        self.number = number
        self.position = position
        self.swung = swung
        self.strikes = strikes
        self.balls = balls
        self.hit = hit
        self.out = out
        self.walked = walked

    def swing(self):
        swing_chance = 0.6
        if random.random() < swing_chance:
            self.swung = True
        else:
            self.swung = False

    def result(self, ball: Ball):
        if ball.hit:
            self.hit = True
            print("That's a hit!")
            return self.hit
        if self.strikes == 3:
            self.out = True
            print(f"{self.name} struck out!")
            return self.out
        elif self.balls == 4:
            self.walked = True
            print("Ball 4, that's a walk.")
            return self.walked


def at_bat(player: Player, ball: Ball):
    """Simulate a player's at bat"""
    print(f"Now batting, number {player.number}, {player.name}!")
    while not player.out:
        ball.pitch()
        player.swing()
        if ball.strike and player.swung:
            ball.hit = True  # hit
            player.result(ball)
        elif ball.strike and not player.swung:
            ball.hit = False  # miss
            player.strikes += 1  # strike
            print(f"Strike {player.strikes}!")
            player.result(ball)
        elif not ball.strike and player.swung:
            ball.hit = False
            player.strikes += 1  # strike
            print(f"Strike {player.strikes}!")
            player.result(ball)
        elif not ball.strike and not player.swung:
            ball.hit = False
            player.balls += 1  # ball
            player.result(ball)


def create_roster(players: str):
    """Create a list of players from a json file"""
    with open(players) as f:
        roster = json.load(f)
    for i in range(len(roster)):
        roster[i] = Player(roster[i]['name'], roster[i]["number"], roster[i]['position'], None, 0, 0, False, False,
                           False)
    return roster


def main():
    """creates the roster of players"""
    roster = create_roster("roster.json")
    print(at_bat(roster[0], Ball(False, False, False, True)))


if __name__ == "__main__":
    main()
