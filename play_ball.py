import setup

innings = 1


def main():
    setup.create_roster("roster.json")
    game = setup.Game((setup.create_roster("roster.json"), 1), (setup.create_roster("roster.json"), 2), 0, 1, 0, 0, 0)


if __name__ == "__main__":
    main()
