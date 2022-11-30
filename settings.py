"""Create classes, etc"""
import json
import random
import time


class Field:
    """creates an object to keep track of the field state, runners, etc"""

    def __init__(self, on_first, on_second, on_third, home, dugout):
        self.on_first = on_first
        self.on_second = on_second
        self.on_third = on_third
        self.scored = home
        self.dugout = dugout


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
        return self.strike


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
        return self.swung


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

    def result(self, ball: Ball, strike: bool, swing: bool):
        if strike and swing:
            ball.hit = True
        elif strike and not swing:
            self.strikes += 1
            print(f"Strike {self.strikes}!")
        elif not strike and swing:
            self.strikes += 1
            print(f"Strike {self.strikes}!")
        elif not strike and not swing:
            self.balls += 1
            print(f"Ball {self.balls}!")

    def at_bat(self, player: Player, ball: Ball):
        """Simulate a player's at bat"""
        print(f"Now batting, number {player.number}, {player.name}!")
        ball.hit = False
        while self.strikes < 3 and self.balls < 4:
            time.sleep(1)
            self.result(ball, ball.pitch(), player.swing())
            if ball.hit:
                print("Hit!")
                break
        if self.strikes == 3:
            self.outs += 1
            self.strikes = 0
            self.balls = 0
            print("Strike 3, you're out!")


def create_roster(team: str, roster: str, ) -> object:
    """Create a list of players from a json file
    :param team:
    :param roster:
    :return:
    """
    players = []
    with open(roster) as f:
        info = json.load(f)
    team_info = [info[team]['name'], info[team]['abbreviation']]
    for i in range(len(info[team]["players"])):
        players.append(Player(info[team]["players"][i]['name'], info[team]["players"][i]["number"],
                              info[team]["players"][i]['position'], None, False, False, False))
    return team_info, players


def main():
    """creates the roster of players"""
    home_team_name, home_team_players = create_roster("home_team", "roster.json")
    away_team_name, away_team_players = create_roster("away_team", "roster.json")
    print(f"{home_team_name[0]}: \n", *home_team_players, sep="\n", end="\n\n")
    print(f"{away_team_name[0]}: \n", *away_team_players, sep="\n", end="\n\n")


if __name__ == "__main__":
    main()
