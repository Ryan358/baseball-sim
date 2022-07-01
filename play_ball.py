import setup

innings = 1


def main():
    home_team_name, home_team_players = setup.create_roster("home_team", "roster.json")
    away_team_name, away_team_players = setup.create_roster("away_team", "roster.json")
    print(f"{home_team_name[0]}: \n", *home_team_players, sep="\n", end="\n\n")
    print(f"{away_team_name[0]}: \n", *away_team_players, sep="\n", end="\n\n")

    game = setup.Game(home_team_name, away_team_name, 0, 1, 0, 0, 0)
    ball = setup.Ball(False, False, False, False)
    for i in range(innings):
        while game.outs < 3:
            while game.strikes < 3:
                for player in home_team_players:
                    game.at_bat(player, ball)
                    if game.out:
                        break
                if game.out:
                    break
                for player in away_team_players:
                    game.at_bat(player, ball)
                    if game.out:
                        break
                if game.out:
                    break


if __name__ == "__main__":
    main()
