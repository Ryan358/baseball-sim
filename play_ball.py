import settings

innings = 1


def main():
    home_team_name, home_team_players = settings.create_roster("home_team", "roster.json")
    away_team_name, away_team_players = settings.create_roster("away_team", "roster.json")
    game = settings.Game(home_team_name, away_team_name, 0, 1, 0, 0, 0)
    print(f"{home_team_name[0]}: \n", *home_team_players, sep="\n", end="\n\n")
    print(f"{away_team_name[0]}: \n", *away_team_players, sep="\n", end="\n\n")

    ball = settings.Ball(False, False, False, False)
    field = settings.Field(None, None, None, None, home_team_players+away_team_players)
    print("------------------------------------------------------------ \n\n")
    game.at_bat(home_team_players[0], ball)
    return ball.hit


if __name__ == "__main__":
    main()
