#!/usr/bin/env python


from brain_games import engine, games


def main():
    """Run a game."""
    engine.run(games.calc)


if __name__ == '__main__':
    main()