"""Create classes, etc"""
import json
import random
import time


class Field:
    """creates an object to keep track of the field state, runners, etc"""

    def __init__(self, bases: dict):
        self.bases = bases


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

    def __init__(self, name, number, team, position, swung, hit, out, walked):
        self.name = name
        self.number = number
        self.team = team
        self.position = position
        self.swung = swung
        self.hit = hit
        self.out = out
        self.walked = walked

    def __str__(self):
        return f"{self.name}, number {self.number}, position {self.position}"

    def swing(self, ball: Ball):
        if ball.strike:
            swing_chance = 0.65
        else:
            swing_chance = 0.30
        if random.random() < swing_chance:
            self.swung = True
        else:
            self.swung = False
        return self.swung


class Game:
    """Create a game state object"""

    def __init__(self, home_team, away_team, field: Field, score: dict, inning, batting_order, outs, balls, strikes):
        self.home_team = home_team
        self.away_team = away_team
        self.field = field
        self.score = score
        self.inning = inning
        self.order = batting_order
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

    def fielding(self, ball: Ball):
        if random.random() < 0.69:
            ball.caught = True
            self.outs += 1
            print("Caught! You're out!")
        else:
            ball.caught = False
        return ball.caught

    def clear_count(self):
        self.strikes = 0
        self.balls = 0

    def advance_runners(self, player: Player, field: Field):
        field.bases["home"] = field.bases["third"]
        field.bases["third"] = field.bases["second"]
        field.bases["second"] = field.bases["first"]
        field.bases["first"] = player
        if field.bases["home"] is not None:
            print(f"{field.bases['home'].name} scores!")
            self.score[player.team] += 1
            field.bases["home"] = None

    def at_bat(self, player: Player, ball: Ball, field: Field):
        """Simulate a player's at bat"""
        print(f"Now batting, number {player.number}, {player.name}!")
        ball.hit = False
        while self.strikes < 3 and self.balls < 4:
            time.sleep(1)
            self.result(ball, ball.pitch(), player.swing(ball))
            if ball.hit:
                print("Hit!")
                self.clear_count()
                time.sleep(1)
                self.fielding(ball)
                if not ball.caught:
                    self.advance_runners(player, field)
                break
        if self.strikes == 3:
            self.outs += 1
            self.clear_count()
            print("You're out!")
            time.sleep(1)
        elif self.balls == 4:
            self.clear_count()
            player.walked = True
            self.advance_runners(player, field)
            print("Walked!")
            time.sleep(1)

    def inning_half(self, team, field: Field):
        while self.outs < 3:
            self.at_bat(team[self.order[team[0].team]], Ball(False, False, False, False), field)
            self.order[team[0].team] += 1
            if self.order[team[0].team] == 9:
                self.order[team[0].team] = 0
        self.outs = 0
        field.bases["first"] = None
        field.bases["second"] = None
        field.bases["third"] = None
        field.bases["home"] = None
        print("Switching sides!")
        time.sleep(1)

    def inning_change(self, home_team, away_team):
        self.inning += 1
        self.outs = 0
        self.clear_count()
        print(f"Top of the {self.inning}th inning! The score is {self.score[home_team[0].team]} to "
              f"{self.score[away_team[0].team]}")
        time.sleep(1)

    def play_inning(self, home, away, field: Field):
        self.inning_half(home, field)
        self.inning_half(away, field)
        self.inning_change(home, away)


def create_roster(team: str, roster: str, ) -> object:
    """Create a list of players from a json file"""
    players = []
    with open(roster) as f:
        info = json.load(f)
    team_info = [info[team]['name'], info[team]['abbreviation']]
    for i in range(len(info[team]["players"])):
        players.append(Player(info[team]["players"][i]['name'], info[team]["players"][i]["number"], info[team]["name"],
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
