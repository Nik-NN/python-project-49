#!/usr/bin/env python3

from brain_games.games import game_progression
from brain_games.logic import games_logic


def main():
    games_logic.engine(game_progression)


if __name__ == '__main__':
    main()
