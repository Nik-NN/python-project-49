#!/usr/bin/env python3

from brain_games.games import game_even
from brain_games.logic import games_logic


def main():
    games_logic.engine(game_even)


if __name__ == '__main__':
    main()
