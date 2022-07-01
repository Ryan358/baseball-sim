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
    """Create a player class with a name, position, swung, hits, and out status"""

    def __init__(self, name, number, position, swung, hit, out, walked):
        self.name = name
        self.number = number
        self.position = position
        self.swung = swung
        self.hit = hit
        self.out = out
        self.walked = walked

    def __str__(self):
        return f"{self.name}, number {self.number}, position {self.position}"

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


class Game:
    """Create a game state object"""

    def __init__(self, home_team, away_team, score, inning, outs, balls, strikes):
        self.home_team = home_team
        self.away_team = away_team
        self.score = score
        self.inning = inning
        self.outs = outs
        self.balls = balls
        self.strikes = strikes

    def at_bat(self, player: Player, ball: Ball):
        """Simulate a player's at bat"""
        print(f"Now batting, number {self.number}, {self.name}!")
        ball.pitch()
        player.swing()
        player.result(ball)


class Field:
    """creates an object to keep track of the field state, runners, etc"""

    def __init__(self, on_first, on_second, on_third, scored, dugout):
        self.on_first = on_first
        self.on_second = on_second
        self.on_third = on_third
        self.scored = scored
        self.dugout = dugout


def create_roster(team: str, roster: str, ) -> object:
    """Create a list of players from a json file"""
    players = []
    with open(roster) as f:
        info = json.load(f)
    for i in range(len(info[team]["players"])):
        players[i] = Player(info[team]["players"][i]['name'], info[team]["players"][i]["number"],
                            info[team]["players"][i]['position'], None, False, False, False)
    return info[team]["players"]


def main():
    """creates the roster of players"""
    home_team = create_roster("home_team", "roster.json")
    print(home_team)


if __name__ == "__main__":
    main()