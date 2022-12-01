import settings

innings = 1


def main():
    home_team_name, home_team_players = settings.create_roster("home_team", "roster.json")
    away_team_name, away_team_players = settings.create_roster("away_team", "roster.json")
    field = settings.Field({"first": None, "second": None, "third": None, "home": None})
    game = settings.Game(home_team_name, away_team_name, field, {away_team_name[0]: 0, home_team_name[0]: 0}, 1,
                         {away_team_name[0]: 0, home_team_name[0]: 0}, 0, 0, 0)
    print(f"{home_team_name[0]}: \n", *home_team_players, sep="\n", end="\n\n")
    print(f"{away_team_name[0]}: \n", *away_team_players, sep="\n", end="\n\n")

    ball = settings.Ball(False, False, False, False)

    print("------------------------------------------------------------ \n\n")
    game.play_inning(home_team_players, away_team_players, field)


if __name__ == "__main__":
    main()
